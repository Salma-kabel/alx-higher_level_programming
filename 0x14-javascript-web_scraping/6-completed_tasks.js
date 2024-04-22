#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    list = JSON.parse(body);
    let dict = {};
    for (let i = 0; i < list.length; i++) {
      if (list[i].completed === true) {
        if (!(Object.prototype.hasOwnProperty.call(dict, list[i].userId))) {
          dict[list[i].userId] = 1;
        } else {
          dict[list[i].userId]++;
        }
      }
    }
    console.log(dict);
  }
});
