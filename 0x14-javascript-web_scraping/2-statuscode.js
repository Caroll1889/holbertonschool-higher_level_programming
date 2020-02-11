#!/usr/bin/node

const request = require('request');
const MyArgs = process.argv.slice(2);

request(MyArgs[0], function (err, response) {
  if (err) {
    return console.log(err);
  } else {
    console.log('code: ' + response.statusCode);
  }
});
