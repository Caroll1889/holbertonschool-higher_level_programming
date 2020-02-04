#!/usr/bin/node

const Myargs = process.argv.slice(2);

if (!Myargs) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < Myargs[0]; i++) {
    console.log('C is fun');
  }
}
