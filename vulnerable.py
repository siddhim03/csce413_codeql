const express = require('express');
const app = express();
const mysql = require('mysql');

const connection = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: '',
  database: 'testdb'
});

app.get('/user', (req, res) => {
  const userId = req.query.id;  // User input not sanitized
  connection.query(`SELECT * FROM users WHERE id = ${userId}`, (err, results) => {
    if (err) throw err;
    res.send(results);
  });
});

app.listen(3000, () => console.log('Server running on port 3000'));
