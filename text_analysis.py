subscription_key = "1jjYlMRmYKOnFdwsko8IEQ6z1E5oniBB2GTjsBCM7LSglljwZQTuJQQJ99BAACYeBjFXJ3w3AAAaACOGcmjw"
assert subscription_key

text_analytics_base_url = "https://eastus.api.cognitive.microsoft.com/text/analytics/v2.0/"
sentiment_api_url = text_analytics_base_url + "sentiment"
documents = {'documents' : [ {'id': '1', 'text': 'I am excited about using AI offerings by microsoft.'},
                            ]}

import requests
headers = {"Ocp-Apim-Subscription-Key": subscription_key}
response = requests.post(sentiment_api_url, headers=headers,
                         json=documents)
languages = response.json()
print(languages)
key_phrase_api_url = text_analytics_base_url + "keyPhrases"
response = requests.post(key_phrase_api_url, headers=headers,
                         json=documents)
key_phrases = response.json()
print(key_phrases)

entity_linking_api_url = text_analytics_base_url + "entities"
response = requests.post(entity_linking_api_url, headers=headers, json=documents)
entities = response.json()
print(entities)