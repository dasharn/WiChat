from flask import Flask, render_template, request, session, redirect, url_for
from flask_socketio import SocketIO, join_room, leave_room, send
from datetime import datetime
import random
import string

app = Flask(__name__)
app.config["SECRET_KEY"] = "agsrsgrwsg"
socketio = SocketIO(app)

rooms = {}


def generate_code(length):
    characters = string.ascii_uppercase + string.digits
    while True:
        code = ''.join(random.choice(characters) for _ in range(length))
        if code not in rooms:
            break
    return code


@app.route("/", methods=["POST", "GET"])
def home():
    session.clear()
    if request.method == "POST":
        name = request.form.get("name")
        code = request.form.get("code")
        join = request.form.get("join", False)
        create = request.form.get("create", False)
        if not name:
            return render_template("home.html", error="Please enter a name.", code=code, name=name)
        if join and not code:
            return render_template("home.html", error="Please enter a room code.", code=code, name=name)
        room = code
        if create:
            room = generate_code(4)
            rooms[room] = {"members": 0, "messages": []}
        elif code not in rooms:
            return render_template("home.html", error="Room does not exist.", code=code, name=name)
        session["room"] = room
        session["name"] = name
        return redirect(url_for("room"))
    return render_template("home.html")


@app.route("/room")
def room():
    room = session.get("room")
    if not all([room, session.get("name"), room in rooms]):
        return redirect(url_for("home"))
    return render_template("room.html", code=room, messages=rooms[room]["messages"])


@socketio.on("message")
def handle_message(data):
    room = session.get("room")
    if room not in rooms:
        return
    timestamp = datetime.now().strftime("%H:%M %p, %d %B %Y")
    content = {"name": session.get("name"), "message": data["data"], "timestamp": timestamp}
    send(content, to=room)
    rooms[room]["messages"].append(content)
    print(f"{session.get('name')} said: {data['data']}")


@socketio.on("connect")
def handle_connect(auth):
    room = session.get("room")
    name = session.get("name")
    if not all([room, name]):
        return
    if room not in rooms:
        leave_room(room)
        return
    join_room(room)
    send({"name": name, "message": "has entered the room"}, to=room)
    rooms[room]["members"] += 1
    print(f"{name} joined room {room}")


@socketio.on("disconnect")
def handle_disconnect():
    room = session.get("room")
    name = session.get("name")
    leave_room(room)
    if room in rooms:
        rooms[room]["members"] -= 1
        if rooms[room]["members"] <= 0:
            del rooms[room]
    send({"name": name, "message": "has left the room"}, to=room)
    print(f"{name} has left the room {room}")


if __name__ == "__main__":
    socketio.run(app, debug=True)