import requests
import json

def emotion_detector(text_to_analyse):
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    Headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    Input_json = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(URL, json = Input_json, headers=Headers)
    formatted_response = json.loads(response.text)
    formatted_response = formatted_response["emotionPredictions"][0]["emotion"] 
    dominant_emotion = max(formatted_response, key=formatted_response.get)
    formatted_response["dominant_emotion"] = dominant_emotion
    return formatted_response