//Same Stuff
const number: string = prompt('Insert a bin number: ');
let counter: number = 0;
let total: number = 0;

for (let i: number = number.length - 1; i >= 0; i--) {
  const c: string = number[i];
  if (c === '1') {
    total += 2 ** counter;
  }
  counter++;
}

console.log(total);
