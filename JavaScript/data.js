function storeStatus() {
    var status = document.getElementById("")
    sessionStorage.setItem("machineStatus", status);
}

function storeUser(user) {
    sessionStorage.setItem("machineUser", user)
}

function storeTime(time) {
    sessionStorage.setItem("machineTime", time)
}

function submission() {

}

function output(location) {
    var output = sessionStorage.getItem(location);
    document.write(output);
}