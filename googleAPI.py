import os
from google.cloud import vision
import pandas as pd

# Set the environment variable for authentication
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/Users/shaveenbageloo/Downloads/pdf2csv-430817-933f52d23f5c.json'

# Initialize the Vision API client
client = vision.ImageAnnotatorClient()

# Function to detect text in an image
def detect_text(image_path):
    with open(image_path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)
    response = client.text_detection(image=image)
    texts = response.text_annotations

    if response.error.message:
        raise Exception(f'{response.error.message}')

    return texts

# Extract text from an image
texts = detect_text('/Users/shaveenbageloo/Downloads/Angelique Grieve.png')

# Convert to JSON-like format
data = []
for text in texts:
    entry = {
        "description": text.description,
        "bounding_poly": text.bounding_poly.vertices
    }
    data.append(entry)

# Convert to DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
print(df)

# Save to CSV
df.to_csv('output.csv', index=False)
