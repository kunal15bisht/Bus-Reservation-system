// Trigger calculation on keyup event
document.getElementById("No_of_person").addEventListener("keyup", calculateAmount);

function calculateAmount() {
const price = parseFloat(document.getElementById("price").value) || 0;
const numberOfPersons = parseInt(document.getElementById("No_of_person").value) || 0;

const totalAmount = price * numberOfPersons;
document.getElementById("amount").value = totalAmount.toFixed(2); // show 2 decimal places
}