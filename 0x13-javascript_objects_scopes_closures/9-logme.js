#!/usr/bin/node
exports.logMe = function (item) {
  let count = 0;
  return function () {
    count++;
    console.log(count + ': ' + item);
  }
}
