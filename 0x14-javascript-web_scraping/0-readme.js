#!/usr/bin/node

const fs = require('fs');
const MyArgs = process.argv.slice(2);

fs.readFile(MyArgs[0], 'utf8', function (err, data) {
  if (err) {
    return console.log(err);
  } else {
    process.stdout.write(data);
  }
});
