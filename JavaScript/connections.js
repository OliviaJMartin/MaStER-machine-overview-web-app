//function to output the machine chosen on each page.
function outputMachine() {
    var machineName = sessionStorage.getItem("machineName");
    document.write(machineName);
}

//function to move from the users current page to the overview page
function overview() {
    location.href = "http://localhost:63342/MaStER-machine-overview-web-app1/templates/Overview.html?_ijt=th9rde00p82sa3m7n48uo4l42d";
}

//function to move from the users current page to the login page
function login(machineName) {
    location.href = "http://localhost:63342/MaStER-machine-overview-web-app1/templates/Login.html?_ijt=th9rde00p82sa3m7n48uo4l42d";
    sessionStorage.setItem("machineName", machineName);
}

//function to move from the users current page to the machine status page
function machineStatus(){
    location.href = "http://localhost:63342/MaStER-machine-overview-web-app1/templates/MachineStatus.html?_ijt=th9rde00p82sa3m7n48uo4l42d";
}

//function to move from the users current page to the update status page
function updateStatus(){
    location.href = "http://localhost:63342/MaStER-machine-overview-web-app1/templates/UpdateStatus.html?_ijt=th9rde00p82sa3m7n48uo4l42d";
}