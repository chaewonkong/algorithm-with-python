// JavaScript - Node.js Algorithm for FESTIVAL Problem

function sum(arr) {
  let sumTotal = 0;
  for (let i = 0; i < arr.length; i++) {
    sumTotal += arr[i];
  }
  return sumTotal;
}

function minAvgPrice(N, L, arrPrice) {
  let days = L;
  let minAvg = sum(arrPrice) / days;
  while (days <= N) {
    let start = 0;
    let end = days;
    while (end <= N) {
      let eachAvg = sum(arrPrice.slice(start, end)) / days;
      if (minAvg > eachAvg) {
        minAvg = eachAvg;
      }
      start += 1;
      end += 1;
    }
    days += 1;
  }
  return minAvg;
}

// Get input and return results
const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

let arr = [];

rl.on("line", input => {
  arr.push(input);
  rl.close();
});
