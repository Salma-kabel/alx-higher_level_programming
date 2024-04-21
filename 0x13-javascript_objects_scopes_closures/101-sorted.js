#!/usr/bin/node
const dict = require('./101-data.js').dict;
const dict2 = {};
for (const element in dict) {
  if (!(Object.prototype.hasOwnProperty.call(dict2, dict[element]))) {
    dict2[dict[element]] = [element];
  } else {
    dict2[dict[element]].push(element);
  }
}
console.log(dict2);
