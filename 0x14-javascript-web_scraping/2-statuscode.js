#!/usr/bin/node
url = process.argv[2];
const request = new Request(url);
const response = fetch(request);
console.log('code: ' + response.status);
