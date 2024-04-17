#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w <= 0) {
      this.width = {};
    } else {
      this.width = w;
    }
    if (h <= 0) {
      this.height = {};
    } else {
      this.height = h;
    }
  }
}
module.exports = Rectangle;
