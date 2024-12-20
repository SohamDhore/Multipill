from flask import Flask, render_template, request, jsonify
import speech_recognition as sr
import sqlite3

app = Flask(__name__)

# Initialize database
def init_db():
    conn = sqlite3.connect('voice_data.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS transcriptions (id INTEGER PRIMARY KEY, text TEXT)''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start-recording', methods=['POST'])
def start_recording():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Recording...")
        audio_data = recognizer.listen(source, timeout=10, phrase_time_limit=10)
        print("Recording stopped.")
    
    try:
        text = recognizer.recognize_google(audio_data)
        print(f"Recognized Text: {text}")
        
        # Store text in the database
        conn = sqlite3.connect('voice_data.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO transcriptions (text) VALUES (?)", (text,))
        conn.commit()
        conn.close()
        
        return jsonify({'status': 'success', 'text': text})
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'status': 'error', 'message': str(e)})

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
