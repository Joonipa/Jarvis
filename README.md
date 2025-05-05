
# Jarvis - Voice-Controlled AI Assistant (Python 3.10 Compatible)

Jarvis is a basic voice-controlled AI assistant built with Python. It can respond to voice commands, search Wikipedia, open websites, play music, and send emails.

## Features

- Voice greeting based on the time of day
- Voice input using microphone
- Text-to-speech responses
- Wikipedia search
- Opens YouTube, Google, Stack Overflow
- Plays music from local folder
- Tells current time
- Sends emails (with login credentials)

## Requirements

- Python 3.10
- Install the required packages:
  ```bash
  pip install pyttsx3 SpeechRecognition wikipedia pyaudio


> If `pyaudio` gives an error, install it using pipwin:

```bash
pip install pipwin
pipwin install pyaudio
```

## How to Run

1. Clone or download this repository.
2. Open a terminal or command prompt.
3. Run the script:

   ```bash
   python jarvis.py
   ```
4. Speak your commands like:

   * “Wikipedia Elon Musk”
   * “Open YouTube”
   * “What’s the time”
   * “Play music”
   * “Send email to Harry”
   * “Exit”

## Setup for Email Sending

1. Replace the placeholder in `sendEmail()` with your real email and app password:

   ```python
   server.login('youremail@gmail.com', 'your-app-password')
   ```

   > For Gmail, turn on 2-step verification and use an [App Password](https://myaccount.google.com/apppasswords).

## Important Notes

* Make sure your microphone is working.
* Update `music_dir` and `codePath` to match your PC’s folder structure.
* Run in a quiet environment for better speech recognition.

## Future Plans

* Add GUI with Tkinter
* Add more voice features like weather, notes, reminders
