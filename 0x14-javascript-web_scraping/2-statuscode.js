#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const req = new Request(url);
const response = fetch(req);
console.log('code: ' + response.status);
