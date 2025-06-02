window.addEventListener('load', setup);

function setup() {
    getDomReferences();
    addEventListeners();
}

function getDomReferences() {
    hamburgerButton = document.getElementById("sidebar-hamburger");
    sidebar = document.getElementById("sidebar1");
}

function addEventListeners() {
    hamburgerButton.addEventListener("click", sidebar_toggle);
}

function sidebar_toggle() {
    if (sidebar.style.display === "none") {
        sidebar.style.display = "block";
        hamburgerButton.setAttribute('title', 'Hide Navigation Menu');
    }
    else {
        sidebar.style.display = "none";
        hamburgerButton.setAttribute('title', 'Show Navigation Menu');
    }
}