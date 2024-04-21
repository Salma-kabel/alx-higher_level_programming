#!/usr/bin/node
const list = require ('./100-data.js');
console.log(list);
const arr = list.map((x, i) => x * i);
console.log(arr);
