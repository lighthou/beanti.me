var socket = io.connect('http://' + document.domain + ':' + location.port);
Notification.requestPermission();


function buttonClicked(event) {
    socket.emit("coffee run", "I want coffee")
}


socket.on("Coffee", function (event) {
    new Notification("Coffee is on. Lets go! ");

})

