#!/usr/bin/node

const MyArgs = process.argv.slice(2);

if (MyArgs < 1) {
  console.log('No argument');
} else {
  console.log(MyArgs[0]);
}
