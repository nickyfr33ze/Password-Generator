const generatedPassword = document.querySelector('generated-password');
const generateButton = document.querySelector('generate-button');
const copyButton = document.querySelector('copy-button');
const lengthInput = document.querySelector('length-input');
const uppercaseElement = document.querySelector('uppercase');
const lowercaseElement = document.querySelector('lowercase');
const numbersElement = document.querySelector('numbers');
const symbolsElement = document.querySelector('symbols');

// const characters = {
//     uppercase: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
//     lowercase: 'abcdefghijklmnopqrstuvwxyz',
//     numbers: '0123456789',
//     symbols: '!@#$%^&*()_+'
// };

function generate() {
    var length = document.getElementById('length').value; // Get the desired password length
    var charset = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=,./<>?;:[]\\|'; // All possible characters
    var password = '';
    for (var i = 0; i < length; i++) {
        password += charset[Math.floor(Math.random() * charset.length)]; // Add a random character to the password
    }
    document.getElementById('password').value = password; // Set the value of the password field to the generated password
}

const updateSlider = () => {
    // update slider value and color
}

generateButton.addEventListener('click', generatePassword);
// add event listener for copy button

copyButton.addEventListener('click', () => {
    // copy generated password to clipboard
    const passwordToCopy = generatedPassword.textContent;
    navigator.clipboard.writeText(passwordToCopy);

    // alert user that password was copied
    alert('Password copied to clipboard');

    // remove alert after 2 seconds
    setTimeout(() => { alert(''); }, 2000);

    // clear selection
    window.getSelection().removeAllRanges();

    // change button text to 'copied'
    copyButton.textContent = 'Copied';

    // change button color to green
    copyButton.style.backgroundColor = 'green';

    // change button text back to 'copy' after 2 seconds
    setTimeout(() => {
        copyButton.textContent = 'Copy';
        copyButton.style.backgroundColor = '';
    }, 2000);
});

lengthInput.addEventListener('input', updateSlider);
// depending on 'input' value, change the slider color and position on the webpage