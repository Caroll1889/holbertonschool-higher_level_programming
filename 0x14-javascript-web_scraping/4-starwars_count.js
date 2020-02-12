#!/usr/bin/node

const request = require('request');
const url = process.argv.slice(2);
let num = 0;

request(url[0], (err, response, body) => {
  if (err) {
    console.log(err);
  }
  const data = JSON.parse(body);
  for (const res of data.results) {
    for (const chars of res.characters) {
      if (chars.indexOf('people/18/') !== -1) {
        num = num + 1;
      } else {
      }
    }
  }
  console.log(num);
});
