#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const result = JSON.parse(body).results;
    let num = 0;
    for (let i = 0; i < result.length; i++) {
      const characters = result[i].characters;
      for (let j = 0; j < characters.length; j++) {
        if (characters[j].includes('18')) {
          num++;
          break;
        }
      }
    }
    console.log(num);
  }
});
