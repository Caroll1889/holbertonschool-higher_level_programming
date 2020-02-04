#!/usr/bin/node

const Myargs = process.argv.slice(2);

const a = Myargs[0];
const b = Myargs[1];

function add (a, b) {
  const suma = parseInt(a) + parseInt(b);
  return suma;
}
console.log(add(a, b));
