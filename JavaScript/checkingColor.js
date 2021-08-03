var color = null
function checkingColor(status) {
    if (status = "Clinical") {
        color = "green";
    } else if (status = "Clinical with limitations") {
        color = "orangered";
    } else if (status = "On service/PMI") {
        color = "blue"
    } else if (status = "Unserviceable"){
        color = "red"
    }
}