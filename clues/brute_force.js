// init
const form = document.getElementById("form");
const out = document.getElementById("out");

form.addEventListener('submit', (e) => {
    e.preventDefault();
    const entered_password = document.getElementById("password").value;
    if (sha256(entered_password) === "dc0d01f196af11cedf649b02305d3387734a539cc22613ad4a63cd69acd2b498") { // don't actually use sha256 to hash passwords
        // assemble key from password to prevent cheesing
        out.innerHTML = ("<h3>Correct!<h3>");
        out.innerHTML += ("<p>" + entered_password[0] + entered_password[3] + entered_password[6] + entered_password[10] + entered_password[15] + entered_password[18] + entered_password[19] + "</p>");
    } else {
        out.innerHTML = ("<h3>Wrong...</h3>");
        out.innerHTML += ("<button onclick=\"window.location.reload(false)\">Try again</button>");
    }
});