def register_socketio_events(sio):
    @sio.on("join")
    def handle_join(data):
        sio.enter_room(data["sid"], data["room"])

    @sio.on("message")
    def handle_message(data):
        room = data["room"]
        sio.emit("message", data, room=room)
