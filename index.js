// lint here: https://validatejavascript.com/
// responsive example: https://www.w3schools.com/howto/tryit.asp?filename=tryhow_js_topnav
let prevActivePage

let showResponsiveNavOptions = false;
let aboutElement = document.getElementById("About");
let projectElement = document.getElementById("Project");
let contactElement = document.getElementById("Contact");
let activePage = aboutElement;

function mobileToggleNavbar() {
    var x = document.getElementById("navbar");
    if (x.className === "navbarClass") {
        x.className += " responsive";
        showResponsiveNavOptions = true;
    } else {
        x.className = "navbarClass";
        showResponsiveNavOptions = false;
    }
    //hide or show the current page
}
function linkClicked(page){
    if(activePage != page){
        prevActivePage = activePage;
        activePage = page;
    }
}

function updateDisplay(){
    //transition out old page
    //transition in new page
}