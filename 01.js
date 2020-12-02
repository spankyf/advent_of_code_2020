const fs = require('fs');
const { myFunction } = require("./myFunction");
var numbers  = [];

fs.readFile('01.csv', 'utf8', function (err, data) {
  var numbers = data.split(/\r?\n/);
});

numbers.forEach((el, ind) => {
console.log(el);
console.log(ind)});

