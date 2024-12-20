document.getElementById('startBtn').addEventListener('click', function () {
    fetch('/start-recording', { method: 'POST' })
        .then(response => response.json())
        .then(data => {
            if (data.status === 'success') {
                document.getElementById('transcription').textContent = data.text;
            } else {
                document.getElementById('transcription').textContent = "Error: " + data.message;
            }
        })
        .catch(error => {
            document.getElementById('transcription').textContent = "Error: " + error;
        });

    this.disabled = true;
    document.getElementById('stopBtn').disabled = false;
});

document.getElementById('stopBtn').addEventListener('click', function () {
    // Just enable the start button again
    document.getElementById('startBtn').disabled = false;
    this.disabled = true;
});
