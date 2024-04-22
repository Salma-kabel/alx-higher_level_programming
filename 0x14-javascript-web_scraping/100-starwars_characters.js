#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const list = [];
    const characters = JSON.parse(body).characters;
    for (let i = 0; i < characters.length; i++) {
      const idlist = characters[i].split("/");
      const id = idlist[idlist.length - 2];
      request('https://swapi-api.alx-tools.com/api/people/' + id, function (err, response, body) {
        if (err) {
          console.log(err);
        } else {
          list.push(JSON.parse(body).name);
        }
      });
    }
    console.log(list);
  }
});
