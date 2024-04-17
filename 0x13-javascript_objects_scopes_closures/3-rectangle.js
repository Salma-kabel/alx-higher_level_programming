#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
  print() {
    for (let i = 0; i < height; i++) {
      let arr = '';
      for (let j = 0; j < width; j++) {
        arr = arr + 'X';
      }
      console.log(arr);
    }
  }
}
module.exports = Rectangle;
