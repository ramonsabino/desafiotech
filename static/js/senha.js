const passwordInput = document.getElementById('password');
const btnGeneratePassword = document.getElementById('generatePassword');

function generateRandomPassowrd() {
  const password = Math.random().toString(36).substring(2);
  window.alert(`ATENÇÃO: sua senha é: ${password}`)
  passwordInput.value = password;
}

btnGeneratePassword.addEventListener('click', generateRandomPassowrd);


console.log(passwordInput)