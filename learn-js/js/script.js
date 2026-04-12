const divContainer = document.querySelector(".container");
divContainer.style.display = "grid";
divContainer.style.gridTemplateColumns = "repeat(6, 1fr)";
divContainer.style.gap = "8px";

let span;
for (let i = 0; i < 102; i++) {
  span = document.createElement("span");
  span.innerText = i;
  divContainer.appendChild(span);
  span.style.fontSize = "32px";
  span.style.padding = "16px";
  span.style.color = "white";
  span.style.textAlign = "center";
  span.style.backgroundColor = isPrimeEvenOddNumber(i);
}

function isPrimeEvenOddNumber(number) {
  // 1. Check if the number is prime => return "red"
  // 2. Check if the number is even => return "green"
  // 3. Check if the number is odd => return "yellow"
  if (number < 2) {
    // Not a prime number
    return number % 2 === 0 ? "green" : "yellow";
  }

  for (let i = 2; i <= Math.sqrt(number); i++) {
    if (number % i === 0) {
      // Not a prime number
      return number % 2 === 0 ? "green" : "yellow";
    }
  }

  // It's a prime number
  return "red";
}
