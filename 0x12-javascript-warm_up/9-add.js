#!/usr/bin/node
const args = process.argv;
function add(a, b) {
  return a + b;
}
const res = add(Number(args[2]), Number(args[3]));
if (!isNaN(res)) {
  console.log(res);
} else {
  console.log('NaN');
}
