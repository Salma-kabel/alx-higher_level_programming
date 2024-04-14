#!/usr/bin/node
const args = process.argv;
let i = Number(args[2]);
if (isNaN(i)) {
  console.log('Missing size');
} else {
  let j = i;
  let arr = 'X';
  while (j > 1) {
    arr = arr + 'X';
    j--;
  }
  while (i > 0) {
    console.log(arr);
    i--;
  }
}
