#!/usr/bin/node
const dict = require('./101-data.js').dict;
let dict2 = {}
for (const element of dict) {
  if (!dict2.hasOwnProperty(dict[element])) {
    dict2[dict[element]] = [element]
  } else {
    dict2[dict[element]].push(element);
  }
}
console.log(dict2);
