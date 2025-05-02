// Trigger calculation on keyup event
document.getElementById("No_of_person").addEventListener("keyup", calculateAmount);

function calculateAmount() {
const price = parseFloat(document.getElementById("price").value) || 0;
const numberOfPersons = parseInt(document.getElementById("No_of_person").value) || 0;

const totalAmount = price * numberOfPersons;
document.getElementById("amount").value = totalAmount.toFixed(2); // show 2 decimal places
console.log(document.getElementById("amount").value)
console.log(document.getElementById("user").value)
console.log(document.getElementById("bus_name").value)
console.log(document.getElementById("from").value)
console.log(document.getElementById("date").value)
console.log(document.getElementById("price").value)
console.log(document.getElementById("email").value)
console.log(document.getElementById("bus_number").value)
console.log(document.getElementById("to").value)
console.log(document.getElementById("No_of_person").value)
console.log(document.getElementById("time").value)
}