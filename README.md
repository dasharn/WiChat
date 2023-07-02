# Online Chat Application

This is a simple chat application built using Flask and Flask-SocketIO. It allows users to join existing chat rooms or create new ones and engage in real-time messaging with other participants in the same room.

## Features

- Users can enter their name and choose to join an existing chat room or create a new one.
- Chat rooms are identified by unique room codes generated randomly.
- Users can send and receive messages in real-time within the chat room.
- Messages are timestamped and displayed along with the sender's name.
- When a user joins or leaves a room, a system message is displayed in the chat.
- Multiple users can participate in the same room and communicate simultaneously.

## Installation

1. Make sure you have Python installed on your system.
2. Clone the repository or download the source code files.
3. Open a terminal and navigate to the project directory.
4. Create a virtual environment (optional but recommended).
5. Install the required packages by running the following command:

   ```shell
   pip install -r requirements.txt

## Usage
To run this application locally for development purposes, follow these steps: 

1. Execute the following command `python app.py` in the terminal

2. Open your web browser and go to http://localhost:5000 to access the chat application.

3. Enter your name and choose whether to join an existing room or create a new one.

4. If you choose to join an existing room, enter the room code provided by another participant.

5. Start sending and receiving messages in real-time within the chat room.


## Technologies Used

- Python
- Flask
- Flask-SocketIO
- HTML
- CSS
- JavaScript
