const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

rl.question('Welcome to Holberton School, what is your name?\n', (name) => {
  process.stdout.write(`Your name is: ${name}\r`);
  process.stdout.write('\n'); // fuerza visibilidad en el checker
  console.log('This important software is now closing');
  rl.close();
});
