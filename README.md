Voice Recorder Web Application

Overview
This is a Flask-based web application that allows users to record voice using their microphone, transcribe the speech into text, and store the results in a SQLite database for future reference. The application features a simple and intuitive web interface with the following functionalities:

Start Recording: Begin recording voice input.
Stop Recording: End the recording session.
Transcription Display: Display the recognized text from the recording on the webpage.
Database Storage: Save the transcribed text in a SQLite database for later use.

Project Structure:
voice_recorder/
├── app.py                 # Flask backend application
├── requirements.txt       # Python dependencies
├── templates/
│   └── index.html         # Frontend HTML template
├── static/
│   ├── style.css          # CSS styles for the webpage
│   └── script.js          # JavaScript for interactivity

