
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app= Flask("Emotion Detection")
@app.route("/emotionDetector")
def sent_detector():
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    if response["dominant_emotion"] != None: 
        formatted_output = "For the given statement the system response is "
        formatted_output += ", ".join([f"{key}: {value}" for key, value in response.items() if key != "sadness" and key != "dominant_emotion"])
        formatted_output += " and {}: {}".format("sadness", response.get("sadness", ""))
        formatted_output += "{} {}".format(". The dominant emotion is", response.get("dominant_emotion", ""))
        return formatted_output
    else:
        return "Invalid text! Please try again!"



@app.route("/")
def render_index_page():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6000)