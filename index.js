var socket = io.connect('http://' + document.domain + ':' + location.port);

document.addEventListener("DOMContentLoaded", function(event) {
    Notification.requestPermission();


    function buttonClicked(event) {
        socket.emit("coffee run");
    }

    document.getElementById("coffee_now").onclick = function() {
        socket.emit("coffee run");
    }

    document.getElementById("keeness").onchange = function () {
        socket.emit("change score", this.value);
    };


    socket.on("Coffee", function (event) {
        new Notification("Coffee is on. Lets go! ");
    })

    socket.on('connect', function() {
        socket.emit('connected');
    });
});


