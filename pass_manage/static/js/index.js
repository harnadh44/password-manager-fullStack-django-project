const pass = document.getElementById("pass");
const note = document.getElementById("note");
const sub = document.getElementById("submit_id");
const userName = document.getElementById("username");
const gen_pass = document.getElementById("btn");
let p;


function Generate_pass() {
    const letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'];
    const numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'];
    const symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+'];

    let l = "";
    for (let i = 0; i < 4; i++) {
        l += letters[Math.floor(Math.random() * letters.length)];
    }

    for (let i = 0; i < 3; i++) {
        l += numbers[Math.floor(Math.random() * numbers.length)];
    }

    for (let i = 0; i < 2; i++) {
        l += symbols[Math.floor(Math.random() * symbols.length)];
    }

    let passwordArray = l.split('');

    for (let i = passwordArray.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [passwordArray[i], passwordArray[j]] = [passwordArray[j], passwordArray[i]];  // Swap elements
    }

    l = passwordArray.join('')

    console.log(l);

    pass.value = l;


}

// Function to toggle password visibility
function togglePassword() {
    const passField = document.getElementById("pass");
    const showPass = document.getElementById("showPass");

    if (showPass.checked) {
        passField.type = "text";  // Show the password
    } else {
        passField.type = "password";  // Hide the password
    }
}
