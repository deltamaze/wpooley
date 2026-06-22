// lint here: https://validatejavascript.com/
// responsive example: https://www.w3schools.com/howto/tryit.asp?filename=tryhow_js_topnav
let prevActivePage

let showResponsiveNavOptions = false;
let navbar = document.getElementById("navbar");
let activePage = document.getElementById("About");

setTargetPageOnLoad(window.location.hash);

function setTargetPageOnLoad(urlHash) {
    if (urlHash.length < 1) {
        return;
    }
    urlHash = urlHash.substring(1);
    linkClicked(urlHash);
    //check to see if user loaded site in with a #id, if so, set activePage
}

function mobileToggleNavbar() {
    showResponsiveNavOptions = !showResponsiveNavOptions;
    if (showResponsiveNavOptions) {
        navbar.classList.add("responsive");
        activePage.classList.remove("fade-in");
        activePage.classList.add("hide");
    } else {
        navbar.classList.remove("responsive");
        activePage.classList.remove("hide");

    }
    //hide or show the current page
}

function linkClicked(page) {
    showResponsiveNavOptions = false; // hide responsive nav menu
    navbar.classList.remove("responsive");

    selectedPage = document.getElementById(page);
    if (selectedPage === activePage) {
        //no change, un hide/return
        activePage.classList.remove("hide");
        return;
    }

    prevActivePage = activePage;
    activePage = selectedPage;
    //reset classes on prev page/active page
    prevActivePage.classList.remove("hide");
    activePage.classList.remove("hide");
    prevActivePage.classList.remove("fade-out");
    activePage.classList.remove("fade-out");
    prevActivePage.classList.remove("fade-in");
    activePage.classList.remove("fade-in");

    //apply animations
    prevActivePage.classList.add("fade-out");
    activePage.classList.add("fade-in");

}
