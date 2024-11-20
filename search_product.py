import sys
import json
import requests
from bs4 import BeautifulSoup
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/search', methods=['GET'])
def fetch_product_details():
    keyword = request.args.get('keyword')
    
    if not keyword:
        return jsonify({"error": "Keyword is required"}), 400
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0 Safari/537.36"
    }

    url = f"https://www.amazon.in/s?k={keyword}"  # Update URL to search with the keyword on Amazon
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return jsonify({"error": "Failed to fetch products"}), 500

    soup = BeautifulSoup(response.text, 'html.parser')
    products = []

    # Scrape products from Amazon's search results page
    for product in soup.select('.s-result-item'):
        title = product.select_one('h2 a span')
        price = product.select_one('.a-price .a-offscreen')
        image = product.select_one('.s-image')
        link = product.select_one('h2 a')

        if title and price:
            products.append({
                "name": title.text.strip(),
                "price": price.text.strip(),
                "image": image['src'] if image else 'https://via.placeholder.com/150',
                "link": 'https://www.amazon.in' + link['href'] if link else '#'
            })

    return jsonify({"products": products})


if __name__ == "__main__":
    app.run(debug=True, port=5001)  # Running Flask app on port 5001
