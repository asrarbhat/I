console.log("hello world", "how are you doing");

function factorial(integer) {
  if (integer == 0) {
    return 1;
  }
  return integer * factorial(integer - 1);
}
console.log(factorial(5));
