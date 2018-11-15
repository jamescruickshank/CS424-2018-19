

function loadinfo(memberId) {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4) {
            document.getElementById("last_name_value").innerHTML = this.responseText;
        }
    };

    xhttp.open("GET", memberId+"/ajax_last_name", true);
    xhttp.send();
}
