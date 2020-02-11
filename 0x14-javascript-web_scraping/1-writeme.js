#!/usr/bin/node

const fs = require('fs');
const MyArgs = process.argv.slice(2);

fs.writeFile(MyArgs[0], MyArgs[1], 'utf8', function (err) {
  if (err) {
    return console.log(err);
  }
});
