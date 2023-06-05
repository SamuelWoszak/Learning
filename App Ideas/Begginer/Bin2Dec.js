//Same stuff
const number = prompt('Insert a bin number: ');
let counter = 0;
let total = 0;

for (let i = number.length - 1; i >= 0; i--) {
  const c = number[i];
  if (c === '1') {
    total += 2 ** counter;
  }
  counter++;
}

console.log(total);
