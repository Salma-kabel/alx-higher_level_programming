#!/usr/bin/node
const file = process.argv[2];
const str = process.argv[3];
const fs = require('fs');
fs.writeFile(file, str, function (err) {
  if (err) {
    console.log(err);
  }
});
