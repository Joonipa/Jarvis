from flask import Flask, request, jsonify
import datetime
import wikipedia
import webbrowser

app = Flask(__name__)

# Helper function to process queries
def process_query(query):
    query = query.lower()

    if "hello" in query:
        return "Hello, how are you?"
    elif "the time" in query:
        return f"The time is {datetime.datetime.now().strftime('%H:%M:%S')}."
    elif "the date" in query:
        return f"Today's date is {datetime.datetime.now().strftime('%d-%m-%Y')}."
    elif "wikipedia" in query:
        topic = query.replace("wikipedia", "").strip()
        try:
            summary = wikipedia.summary(topic, sentences=2)
            return summary
        except Exception as e:
            return "I couldn't fetch information from Wikipedia. Please try again."
    elif "open youtube" in query:
        webbrowser.open("https://www.youtube.com")
        return "Opening YouTube."
    elif "open google" in query:
        webbrowser.open("https://www.google.com")
        return "Opening Google."
    elif "jarvis quit" in query:
        return "Goodbye! Closing Jarvis."
    else:
        return "I didn't understand that. Please try again."

@app.route("/process", methods=["POST"])
def process():
    data = request.json
    query = data.get("query", "")
    reply = process_query(query)
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)
