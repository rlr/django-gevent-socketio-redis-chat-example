
(function($){

"use strict";

function init() {
    var s = new io.Socket(window.location.hostname, {
      port: 9000,
      rememberTransport: false,
      //transports: ['xhr-multipart', 'xhr-polling'],
      resource: 'socket.io'
    });
    s.connect();

    s.addEvent('connect', function() {
    });

    s.addEvent('message', function(data) {
        var $chatbox = $("#chat-box");
        $chatbox.append("<div>" + data + "</div>").scrollTop($chatbox[0].scrollHeight);
    });

    //send the message when submit is clicked
    $('#chat-form').submit(function (ev) {
        var $this = $(this),
            $textbox = $this.find('[name="message"]'),
            message = $textbox.val();
        ev.preventDefault();
        if (message !== '') {
            $textbox.val('');
            s.send(message);
        }
    });
}

$(document).ready(init);

}(jQuery))