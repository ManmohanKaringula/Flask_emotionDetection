''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app= Flask("Emotion Detection")
@app.route("/emotionDetector")
def sent_detector():
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    formatted_output = "For the given statement the system response is "
    formatted_output += ", ".join([f"{key}: {value}" for key, value in response.items() if key != "sadness" and key != "dominant_emotion"])
    formatted_output += " and {}: {}".format("sadness", response.get("sadness", ""))
    formatted_output += "{} {}".format(". The dominant emotion is", response.get("dominant_emotion", ""))
    return formatted_output




@app.route("/")
def render_index_page():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6000)