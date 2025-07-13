
document.getElementById("loginForm").addEventListener("submit", function (event) {
  event.preventDefault(); // Prevent page reload

  const username = document.getElementById("user").value.trim();
  const password = document.getElementById("pass").value;

  if (!isValidUsername(username)) {
    alert("Invalid username. Use only letters, numbers, and at least 4 characters.");
    return;
  }

  if (!isValidPassword(password)) {
    alert("Weak password. Must include uppercase, number, and special character.");
    return;
  }

  // Simulate a secure login attempt
  console.log("Username:", username);
  console.log("Password:", password); // Don’t do this in real apps!

  alert("Login credentials submitted (simulated). Always use server-side verification in real apps.");
});

function isValidUsername(username) {
  // Minimum 4 characters, letters and numbers only
  const usernameRegex = /^[a-zA-Z0-9]{4,}$/;
  return usernameRegex.test(username);
}

function isValidPassword(password) {
  // At least 8 chars, 1 uppercase, 1 number, 1 special character
  const strongRegex = /^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/;
  return strongRegex.test(password);
}