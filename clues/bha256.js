// init
const form = document.getElementById("form");
const out = document.getElementById("out");

function pad(str) {
    const bigendian = (str.length.toString(2))
    let res = str + "1";
    while ((res.length % 32) != 0) {
        res += "0";
    }
    res = res.slice(0, -64) + "0".repeat(64 - bigendian.length) + bigendian;
    return res;
}

function chunk_num(num) {
    let res = []
    for (let i = 32; i <= num.length; i += 32) {
        res.push(parseInt(num.slice(i-32, i), 2).toString(16));
    }
    return res;
}

function bha256(str) {
    const hasharr = [
        0xb1e938b3,
        0x56c51a8c,
        0xb596d38c,
        0xdb5e45af,
        0x9116261a,
        0x66cb2945,
        0x8c58c8e9,
        0x8cac5e27,
        0xba9288af,
        0xdf27cf8e,
        0x4dd8decc,
        0x5c96d192,
        0xd21fbefa,
        0xcd29b24d,
        0xe3e7dfaa,
        0x81c9bd7f,
        0x584aec7d,
        0xd63f5559,
        0x7a9c4b75,
        0x432444b9,
        0xe99dc4f9,
        0xcf51d833,
        0x6d7a457b,
        0x5ab6cc8c,
        0xd99389fc,
        0xa73e476b,
        0xc9783a3c,
        0x8a71a978,
        0xaffa138e,
        0x69f7da4a,
        0x4f867a49,
        0xdfac54ff
    ];
    const binstr = pad(str.split("").map(char => {
        return char.charCodeAt(0).toString(2);
    }).join(""));
    var h0 = 0x2b338cb2;
    var h1 = 0x57e35421;
    var h2 = 0xc5a2a81d;
    var h3 = 0xc28f8bbc;
    var h4 = 0xcccf222e;
    var h5 = 0x914e777a;
    var h6 = 0xda871d92;
    var h7 = 0x29ecd3d5;
    let hexarr = chunk_num(binstr);
    for (let i = 0; i < hexarr.length; i++) {
        hexarr[i] = parseInt(hexarr[i], 16) ^ hasharr[i % 32];
    }
    h0 = (h0 ^ hexarr[0]).toString(16).slice(1);
    h1 = (h1 ^ hexarr[1]).toString(16).slice(1);
    h2 = (h2 ^ hexarr[2]).toString(16).slice(1);
    h3 = (h3 ^ hexarr[3]).toString(16).slice(1);
    h4 = (h4 ^ hexarr[4]).toString(16).slice(1);
    h5 = (h5 ^ hexarr[5]).toString(16).slice(1);
    h6 = (h6 ^ hexarr[6]).toString(16).slice(1);
    h7 = (h7 ^ hexarr[7]).toString(16).slice(1);
    return h0 + h1 + h2 + h3 + h4 + h5 + h6 + h7;
}

form.addEventListener('submit', (e) => {
    e.preventDefault();
    const data = document.getElementById("data").value;
    out.innerHTML = bha256(data)
});