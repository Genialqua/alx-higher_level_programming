#!/usr/bin/node

const { argv } = require('process');
const myStr = 'My number:';

if (isNaN(argv[2])) {
  console.log('Not a number');
} else {
  console.log(`${myStr} ${parseInt(argv[2])}`);
}
