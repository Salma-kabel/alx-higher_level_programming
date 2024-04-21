#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
 let num = 0;
  for element in list {
    if (element === searchElement) {
      num++;
    }
  }
}
