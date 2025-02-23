const express = require('express');
const app = express();
app.use(express.static('public'));

// Mock database with sample data
let mockData = Array.from({length: 100}, (_, i) => `Item ${i + 1}`);

app.get('/items', (req, res) => {
  const page = parseInt(req.query.page) || 1;
  const pageSize = 20;
  const startIndex = (page - 1) * pageSize;
  const endIndex = startIndex + pageSize;

  const results = {
    data: mockData.slice(startIndex, endIndex),
    page,
    hasMore: endIndex < mockData.length
  };

  // Simulate network delay
  setTimeout(() => res.json(results), 500);
});

app.listen(3000, () => console.log('Server running on port 3000'));
