#!/usr/bin/node
const args = process.argv.slice(2);
const lan = args.length;
if (lan === 0) {
  console.log('No argument');
} else if (lan === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
