#!/usr/bin/node

const MyArgs = process.argv.slice(2);

if (Math.floor(MyArgs[0])) {
  console.log(`My number: ${Math.floor(MyArgs[0])}`);
} else {
  console.log('Not a number')
}
