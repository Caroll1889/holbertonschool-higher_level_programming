#!/usr/bin/node

const Myargs = process.argv.slice(2);

function factorial (n) {
  if (!n) {
    return 1;
  } else {
    return factorial(n - 1) * n;
  }
}
console.log(factorial(Myargs[0]));
