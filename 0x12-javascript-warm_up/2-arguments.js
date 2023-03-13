#!/usr/bin/node

const count = 3;

process.argv.forEach((val) => {
   console.log(`count: ${!val ? 'No argument' : val === process.argv[0] || val === process.argv[1] ? 'Argument found' : 'Arguments found'}`);
});
