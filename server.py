from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector
app = Flask("Emotion Detector")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/emotionDetector")  
def emotion_detection():
    text_to_analyze = request.args.get("textToAnalyze")  
    response = emotion_detector(text_to_analyze)
    print(response)
    return f"For the given statement, the system response is 'anger': {response['anger']}, 'disgust': {response['disgust']}, 'fear': {response['fear']}, 'joy': {response['joy']} and<br>'sadness': {response['sadness']}. The dominant emotion is <b>{response['dominant_emotion']}</b>."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000) 