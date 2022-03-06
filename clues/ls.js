function encodeToken(token) {
    try {
        return btoa(JSON.stringify(token));
    } catch (e) {
        return undefined;
    };
};

function decodeToken(token) {
    try {
        return JSON.parse(atob(token));
    } catch (e) {
        return undefined;
    }
}

if (decodeToken(window.localStorage["token"]) === undefined) {
    window.localStorage.setItem("token", encodeToken({ "auth": false }));
};

setTimeout(function () {
    if (decodeToken(window.localStorage["token"])["auth"]) {
        document.getElementById("name").innerHTML = "Correct.";
        document.getElementById("message").innerHTML = "stop"[0] + "looking at th3 source code"[13] + window.localStorage["token"][3] + "svperman is worst superhero"[1] + window.localStorage["token"][16] + "133t sp34k"[8] + "you can stop now"[9];
    } else {
        document.getElementById("name").innerHTML = "Access denied.";
        document.getElementById("message").innerHTML = "Access denied.";
    };
}, 1000);