function login() {
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;

    if (username === "yourusername" && password === "yourpassword") {
        alert("Login successful!");
    } else {
        alert("Invalid username or password.");
    }
}
