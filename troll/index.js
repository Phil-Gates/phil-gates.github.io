// SOME OF THIS CODE IS FROM https://github.com/feross/TheAnnoyingSite.com
HISTORY = [
    "rick astley photos",
    "what to do if you're being stalked",
    "why is rick astley stalking me",
    "rick astley is outside my window",
    "rick astley is in my house",
    "why did rick astley kill my dog",
    "why is rick astley in my house again",
    "please help me",
    "i need to escape from rick astley"
]

function spamHistory(win) {
    var rick;
    if (win == null) {
        return;
    };
    win.window.location = 'https://www.google.com/search?q=' + encodeURIComponent(HISTORY[0]);
    let searchIndex = 1;
    const interval = setInterval(() => {
        if (win.closed) {
            clearInterval(interval);
            document.getElementById("p").innerHTML = "You could not be verified. Reload the page and try again.";
            return;
        }

        setTimeout(() => {
            win.window.location = 'https://www.google.com/search?q=' + encodeURIComponent(HISTORY[searchIndex % HISTORY.length]);
            searchIndex += 1;
            if (!(searchIndex % 3)) {
                for (let i = 0; i < 100; i++) {
                    document.body.appendChild(document.createElement("br"));
                };
                rick = document.createElement("img");
                rick.style.height = "100%";
                rick.style.width = "100%";
                rick.src = "rick.png";
                document.body.appendChild(rick);

                window.print();
            };
        }, 500);
    }, 500);
};

for (let i = 0; i < 30; i++) {
    window.history.pushState({}, "", window.location.pathname + "?rickrolled=" + i);
};

window.history.pushState({}, "", window.location.pathname);

window.addEventListener("popstate", () => {
    window.history.forward();
});

window.onload = function () {
    if (window.opener != null) {
        document.getElementById("b").style = "display: none;";
        document.getElementById("p").innerHTML = "Loading... do not close any tabs...";
        logout = document.createElement("img")
        logout.style.height = "0px";
        logout.style.width = "0px";
        logout.src = "https://google.com/accounts/Logout";
        logout.onerror = "";
        
        spamHistory(window.opener);
    };
};
