#!/usr/bin/node

// A script for arguments
const { argv } = require('process');

if (argv.length <= 2) {
  console.log('No argument');
} else {
  console.log('Arguments found');
}
