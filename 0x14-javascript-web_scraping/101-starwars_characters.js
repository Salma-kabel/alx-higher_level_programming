#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const characters = JSON.parse(body).characters;
    printNames(characters, 0);
  }
});

function printNames (characters, i) {
  if (i >= characters.length) {
    return;
  }
  const idlist = characters[i].split('/');
  const id = idlist[idlist.length - 2];
  request('https://swapi-api.alx-tools.com/api/people/' + id, function (err, response, body) {
    if (err) {
      console.log(err);
    } else {
      console.log(JSON.parse(body).name);
      printNames(characters, i + 1);
    }
  });
}
