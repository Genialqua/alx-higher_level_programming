#!/usr/bin/node

const { argv } = require('process');
const arg1 = argv[2];
const arg2 = argv[3];
const argm = 'is';
const argu = 'undefined';

if (argv[2] === undefined) {
  console.log(`${arg1} ${argm} ${argu}`);
} else {
  console.log(`${arg1} ${argm} ${arg2}`);
}
