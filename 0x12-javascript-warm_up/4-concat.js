#!/usr/bin/node

const Myargs = process.argv.slice(2);

const str1 = Myargs[0];

const str2 = Myargs[1];

const res = `${str1} is ${str2}`;

console.log(res);
