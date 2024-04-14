#!/usr/bin/node
const args = process.argv;
if (args.length < 4) {
  console.log(0);
} else {
  let s;
  let b;
  let i = 2;
  if (+args[i] > +args[i + 1]) {
    b = args[i];
    s = args[i + 1];
  } else {
    b = args[i + 1];
    s = args[i];
  }
  for (i; i < args.length; i++) {
    if (+args[i] > +b) {
      s = b;
      b = args[i];
    } else if (+args[i] > +s && +args[i] < +b) {
      s = args[i];
    }
  }
  console.log(s);
}
