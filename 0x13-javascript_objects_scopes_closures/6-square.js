#!/usr/bin/node
const Squareone = require('./5-square');

class Square extends Squareone {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      let arr = '';
      for (let j = 0; j < this.width; j++) {
        arr = arr + c;
      }
      console.log(arr);
    }
  }
}
module.exports = Square;
