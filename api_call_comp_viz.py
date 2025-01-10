subscription_key = "5pDzzMgNbKSfESEOq5VqEahTALdfef9W6M7HDI1N3AB5sZL0aN8ZJQQJ99BAACYeBjFXJ3w3AAAFACOGPjni"
assert subscription_key


vision_base_url = "https://eastus.api.cognitive.microsoft.com/vision/v1.0/"
vision_analyze_url = vision_base_url + "analyze"
image_url = "https://di-ph.rdtcdn.com/videos/202110/30/397230951/thumbs_5/(m=eaSaaTbWx)(mh=gyufaze87h5IExqE)2.jpg"

import requests
headers = {'Ocp-Apim-Subscription-Key': subscription_key }
params = {'visualFeatures': 'Categories,Description,Color'}
data = {'url': image_url}
response = requests.post(vision_analyze_url, headers=headers, params=params, json=data)
response.raise_for_status()

analysis = response.json()
print(analysis)

image_caption = analysis["description"]["captions"][0]["text"].capitalize()

from PIL import Image
from io import BytesIO
import matplotlib.pyplot as plt

image = Image.open(BytesIO(requests.get(image_url).content))
plt.imshow(image)
plt.axis("off")
_ = plt.title(image_caption, size="x-large", y=-0.1)
