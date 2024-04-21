#!/usr/bin/node
const fs = require('fs');
const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];
const content1 = fs.readFileSync(fileA, 'utf8');
const content2 = fs.readFileSync(fileB, 'utf8');
fs.writeFileSync(fileC, content1 + content2, 'utf8');
