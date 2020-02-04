#!/usr/bin/node

const MyArgs = process.argv.slice(2);

if (MyArgs < 1) {
  console.log('No argument');
} else if (MyArgs.length === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
