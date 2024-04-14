#!/usr/bin/node
const args = process.argv;
let num = Number(args[2]);
function factorial (num) {
  if (num === 1) {
    return 1;
  } else {
    return factorial(num - 1) * num;
  }
}
if (!isNaN(num)) {
  console.log(factorial(num));
} else {
  console.log(1);
}
