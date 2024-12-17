const myFisrtPromise = newPromise((resolve, reject) => {
  setTimeout(() => {
    resolve("Success!");
  }, 250);
});

myFirstPromise.then((successMessage) => {
  console.log(`yay! ${successMessage}`);
});
