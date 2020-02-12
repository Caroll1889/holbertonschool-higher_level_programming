#!/usr/bin/node

const request = require('request');
const url = 'https://jsonplaceholder.typicode.com/todos';

request(url, (err, response, body) => {
  if (err) {
    console.log(err);
  }

  const dict = {};
  const data = JSON.parse(body);
  console.log(data);
  for (const task of data) {
    if (task.completed === true) {
      dict[task.userId] = 0;
    }
  }
  for (const task of data) {
    if (task.completed === true) {
      dict[task.userId] += 1;
    }
  }
  console.log(dict);
});
