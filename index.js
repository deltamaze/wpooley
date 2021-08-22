// lint here: https://validatejavascript.com/
// responsive example: https://www.w3schools.com/howto/tryit.asp?filename=tryhow_js_topnav
function mobileToggleNavbar() {
    var x = document.getElementById("navbar");
    if (x.className === "navbarClass") {
        x.className += " responsive";
    } else {
        x.className = "navbarClass";
    }
}