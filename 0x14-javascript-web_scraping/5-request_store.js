#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const MyArgv = process.argv.slice(2);

request(MyArgv[0], function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    fs.writeFile(MyArgv[1], body, 'utf8', error => { });
  }
});
