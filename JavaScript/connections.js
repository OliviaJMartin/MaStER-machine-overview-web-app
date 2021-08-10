//function to output the machine chosen on each page.
function outputMachine() {
    var machineName = sessionStorage.getItem("machineName");
    document.write(machineName);
}

//function to move from the users current page to the overview page
function overview() {
    location.href = "http://localhost:63342/MaStER-machine-overview-web-app-3/templates/Overview.html?_ijt=a8dvk01a6142d6kn54lc4rsbtr&_ij_reload";
}

//function to move from the users current page to the login page
function login(machineName) {
    location.href = "http://localhost:63342/MaStER-machine-overview-web-app-3/templates/Login.html?_ijt=a8dvk01a6142d6kn54lc4rsbtr&_ij_reload";
    sessionStorage.setItem("machineName", machineName);
}

//function to move from the users current page to the machine status page
function machineStatus(){
    location.href = "http://localhost:63342/MaStER-machine-overview-web-app-3/templates/MachineStatus.html?_ijt=a8dvk01a6142d6kn54lc4rsbtr&_ij_reload";
}

//function to move from the users current page to the update status page
function updateStatus(){
    location.href = "http://localhost:63342/MaStER-machine-overview-web-app-3/templates/UpdateStatus.html?_ijt=a8dvk01a6142d6kn54lc4rsbtr&_ij_reload";
}