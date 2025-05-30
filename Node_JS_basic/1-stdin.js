process.stdin.setEncoding('utf8');

console.log('Welcome to Holberton School, what is your name?');

process.stdin.on('readable', () => {
  const chunk = process.stdin.read();
  if (chunk !== null) {
    const name = chunk.trim();
    if (name) {
      process.stdout.write(`Your name is: ${name}\r`);
    }
  }
});

process.stdin.on('end', () => {
  console.log('This important software is now closing');
});

process.on('SIGINT', () => {
  console.log('\nThis important software is now closing');
  process.exit(0);
});
