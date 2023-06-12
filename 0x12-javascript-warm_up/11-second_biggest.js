#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log(0);
} else {
  const list = process.argv.slice(2);
  let largest = list[0];
  let seclargest = list[0];
  for (let i = 0; i < list.length; i++) {
    if (list[i] > largest) {
      seclargest = largest;
      largest = list[i];
    }
  }
  if (seclargest === largest) {
    console.log(0);
  } else {
    console.log(seclargest);
  }
}
