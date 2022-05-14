function changeText(id) {
    id.innerHTML = "you have changed this text with an 'onclick' event"
}
function displayDate(id) {
    document.getElementById("date").innerHTML = Date();
}
function toggleDM() {
    let element = document.body;
    let mainBox = document.getElementsByClassName("main-box");
    let state = localStorage.getItem("state");
    element.classList.toggle("dark-mode");
    for (const box of mainBox) {
        box.classList.toggle("dark-modeb");
    }
if (state !=="dark") {
    localStorage.setItem("state", "dark");
} else {
    localStorage.setItem("state", "light");
}
}
function darkCheck() {
    let element = document.body;
    let mainBox = document.getElementsByClassName("main-box");
    let state = localStorage.getItem("state");

    if (state == "dark") {
        element.classList.toggle("dark-mode");
        for (const box of mainBox) {
            box.classList.toggle("dark-modeb");
        }
    }
}
function checkCookies() {
    let text = ""
    if (navigator.cookiesEnabled == true) {
        text = "cookies are enabled";
    } else {
        text = "cookies are not enabled";
    }
    document.getElementById("cookie").innerHTML = text;
}
function mOver(obj) {
   obj.innerHTML = "<br> HELLO"
}
function mOut(obj) {
    obj.innerHTML = ""
}
function sendAlert() {
    alert(location.hostname);
}