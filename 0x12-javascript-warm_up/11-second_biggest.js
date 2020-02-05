#!/usr/bin/node

const Myargs = process.argv.slice(2);

if (Myargs.length <= 1) {
  console.log(0);
} else {
  const nums = Myargs.map(value => parseInt(value));
  const max1 = Math.max(...nums);
  const NewList = [];

  for (let i = 0; i < nums.length; i++) {
    if (nums[i] !== max1) {
      NewList.push(nums[i]);
    }
  }
  const max2 = Math.max(...NewList);
  console.log(max2);
}
