const generatedPassword = document.querySelector('generated-password');
const generateButton = document.querySelector('generate-button');
const copyButton = document.querySelector('copy-button');
const lengthInput = document.querySelector('length-input');
const uppercaseElement = document.querySelector('uppercase');
const lowercaseElement = document.querySelector('lowercase');
const numbersElement = document.querySelector('numbers');
const symbolsElement = document.querySelector('symbols');

const characters = {
    uppercase: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
    lowercase: 'abcdefghijklmnopqrstuvwxyz',
    numbers: '0123456789',
    symbols: '!@#$%^&*()_+'
};

const generatePassword = () => {
    const length = lengthInput.value;
    let password = '';
    let generatedPassword = '';

    for (let i = 0; i < length; i++) {
        // fill password input with random characters
        password += characters.uppercase.charAt(Math.floor(Math.random() * characters.uppercase.length));
        password += characters.lowercase.charAt(Math.floor(Math.random() * characters.lowercase.length));
        password += characters.numbers.charAt(Math.floor(Math.random() * characters.numbers.length));
        password += characters.symbols.charAt(Math.floor(Math.random() * characters.symbols.length));

        // shuffle password
        generatedPassword = password.split('').sort(() => Math.random() - 0.5).join('');

        // remove extra characters
        generatedPassword = generatedPassword.slice(0, length);

        // return generated password
        return generatedPassword;
    }
    // set generated password to 'generatedPassword' element
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