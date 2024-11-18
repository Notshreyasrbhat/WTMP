import React, { useState } from 'react';

const PriceTrackerForm = ({ onSubmit }) => {
  const [url, setUrl] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    if (url) {
      onSubmit(url);
      setUrl('');
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input 
        type="url" 
        placeholder="Enter Amazon Product URL" 
        value={url} 
        onChange={(e) => setUrl(e.target.value)} 
        required 
      />
      <button type="submit">Track Price</button>
    </form>
  );
};

export default PriceTrackerForm;
