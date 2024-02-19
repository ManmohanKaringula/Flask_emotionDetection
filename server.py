"""
This module provides a Flask application for emotion detection.
"""

from typing import Dict, Union
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

def generate_emotion_output(response: Dict[str, Union[str, float]]) -> str:
    """
    Generate formatted output based on emotion detection response.
    """
    sadness = response.get("sadness", "")
    dominant_emotion = response.get("dominant_emotion", "")
    details_output = ", ".join([f"{key}: {value}" for key, value in response.items() if key not in ("sadness", "dominant_emotion")])
    emotion_output = f" and sadness: {sadness}" if sadness else ""
    emotion_output += f". The dominant emotion is {dominant_emotion}" if dominant_emotion else ""
    return f"For the given statement, the system response is {details_output}{emotion_output}" if "dominant_emotion" in response else "Invalid text! Please try again!"

@app.route("/emotionDetector")
def emotion_detector_handler() -> str:
    """
    Analyze the provided text and return emotion detection results.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    return generate_emotion_output(response)

@app.route("/")
def render_index_page() -> str:
    """
    Render the index.html template.
    """
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
