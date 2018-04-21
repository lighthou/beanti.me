new Notification("Ok");

var ws = new WebSocket("ws:/localhost:8000/websocket");

ws.onopen = function() {
    ws.send("Hello, world");
    alert("websocket open")
};
ws.onmessage = function (evt) {
    alert(evt.data);
};