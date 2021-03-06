#!/usr/bin/node

const request = require('request');
const url = process.argv.slice(2);

request(url[0], function (err, response, body) {
  if (err) {
    console.log(err);
  }

  const dict = {};
  const data = JSON.parse(body);
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
