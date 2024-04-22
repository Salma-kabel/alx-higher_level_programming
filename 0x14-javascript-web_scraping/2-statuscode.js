#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const req = new request(url);
const response = fetch(req);
console.log('code: ' + response.status);
