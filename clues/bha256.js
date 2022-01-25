// init
const form = document.getElementById("form");
const out = document.getElementById("out");

function pad(str) {
    const bigendian = (str.length.toString(2))
    let res = str + "1";
    while ((res.length % 512) != 0) {
        res += "0";
    }
    res = res.slice(0, -64) + "0".repeat(64 - bigendian.length) + bigendian;
    return res;
}

function chunk_num(num) {
    let res = []
    console.log(num)
    for (let i = 0; i < num.length; i += 512) {
        res.push(parseInt(num.slice(i-512, i), 2).toString(16));
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
    var h0 = 0xf54ce4eafc941582c19c8d78b4a74c63;
    var h1 = 0x225b32b494ba3aaeada2c5f55f73d6b6;
    var h2 = 0xb917b3cc9ffb8118bfc457be9d7641fc;
    var h3 = 0xa347d2a51989f961fd5b45ca256cd5d9;
    var h4 = 0xdd35669af73ec4e785a1e875a358fa91;
    var h5 = 0xf682ec561a1d8b926fa5dbfc9956a122;
    var h6 = 0x99618b5ddf7e5782741c594923b4b94c;
    var h7 = 0x5ba658854b343ac4eefc5d9dd27143fc;
    let hexarr = chunk_num(binstr);
    for (i = 0; i < hexarr.length; i++) {
        hexarr[i] = parseInt(hexarr[i], 16) ^ hasharr[i % 32];
    }
    h0 = (h0 ^ hexarr[0]).toString(16);
    h1 = (h1 ^ hexarr[1]).toString(16);
    h2 = (h2 ^ hexarr[2]).toString(16);
    h3 = (h3 ^ hexarr[3]).toString(16);
    h4 = (h4 ^ hexarr[4]).toString(16);
    h5 = (h5 ^ hexarr[5]).toString(16);
    h6 = (h6 ^ hexarr[6]).toString(16);
    h7 = (h7 ^ hexarr[7]).toString(16);
    return h0 + h1 + h2 + h3 + h4 + h5 + h6 + h7;
}

form.addEventListener('submit', (e) => {
    e.preventDefault();
    const data = document.getElementById("data").value;
    out.innerHTML = bha256(data)
});