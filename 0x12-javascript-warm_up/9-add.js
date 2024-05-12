#!/usr/bin/node

const { argv } = require('process');
const a = parseFloat(argv[2]);
const b = parseFloat(argv[3]);

if (isNaN(argv[2], argv[3])) {
  console.log('NaN');
} else {
  function add (a, b) {
    const result = a + b;
    console.log(result);
  }
  add(a, b);
}
