import React, { useState } from 'react';
import './FeedbackPage.css';

const FeedbackPage = () => {
  const [feedback, setFeedback] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    alert('Thank you for your Valuable feedback!');
    setFeedback('');
  };

  return (
    <div className="feedback-page">
      <h2>Feedback</h2>
      <form onSubmit={handleSubmit}>
        <textarea
          placeholder="We value your feedback"
          value={feedback}
          onChange={(e) => setFeedback(e.target.value)}
          required
        ></textarea>
        <button type="submit">Submit</button>
      </form>
    </div>
  );
};

export default FeedbackPage;
