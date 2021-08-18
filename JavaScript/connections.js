//function to output the machine chosen on each page.
function outputMachine() {
    var machineName = sessionStorage.getItem("machineName");
    document.write(machineName);
}

//function to move from the users current page to the overview page
function overview() {
    location.href = "http://localhost:63342/MaStER-machine-overview-web-app/templates/Overview.html?_ijt=6r5ifbqpqgtsgnpkiaqev6il0c";
}

//function to move from the users current page to the login page
function login(machineName) {
    location.href = "http://localhost:63342/MaStER-machine-overview-web-app/templates/Login.html?_ijt=48tgkeokrci9b2qd09l29lri1m";
    sessionStorage.setItem("machineName", machineName);
}

//function to move from the users current page to the machine status page
function machineStatus(){
    location.href = "http://localhost:63342/MaStER-machine-overview-web-app/templates/MachineStatus.html?_ijt=48tgkeokrci9b2qd09l29lri1m";
}

//function to move from the users current page to the update status page
function updateStatus(){
    location.href = "http://localhost:63342/MaStER-machine-overview-web-app/templates/UpdateStatus.html?_ijt=48tgkeokrci9b2qd09l29lri1m";
}