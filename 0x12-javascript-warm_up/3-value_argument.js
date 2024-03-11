#!/usr/bin/node
const chal = process.argv[2];
if (chal === undefined) {
  console.log('No argument');
} else {
  console.log(chal);
}
