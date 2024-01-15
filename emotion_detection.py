import json
import requests


def emotion_detector(text_to_analyze):
    # Watson NLP Library Emotion Detection API endpoint
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Headers for the API request
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Input JSON for the API request
    input_json = {"raw_document": {"text": text_to_analyze}}

    try:
        response = requests.post(url, headers=headers, json=input_json)
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response

            result = response.json()

            emotion_scores = result['emotionPredictions'][0]['emotion']

            emotion_scores['dominant_emotion'] = max(emotion_scores, key=emotion_scores.get)

            return emotion_scores
        else:
            # Print an error message if the request was not successful
            print(f"Error: {response.status_code} - {response.text}")
            
            return None

    except Exception as e:
        print(f"Error: {e}")
        return None

# Example usage:
# text_to_analyze = "Your text goes here."
# result = emotion_detector(text_to_analyze)
# print(result)
