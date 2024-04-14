#!/usr/bin/node
const args = process.argv;
let i = Number(args[2]);
if (isNaN(i)) {
  console.log('Missing number of occurrences');
} else {
  while (i) {
    console.log('C is fun');
    i--;
  }
}
