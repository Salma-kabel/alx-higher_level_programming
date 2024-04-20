#!/usr/bin/node
const Squareone = require('./5-square');

class Square extends Squareone {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    this.print();
  }
}
module.exports = Square;
