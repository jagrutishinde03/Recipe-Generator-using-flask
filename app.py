from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__, static_url_path='/static')
# Replace this with your actual API key
API_KEY = "sk-51152354400344de95d3866544e43d9b"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    output_type = "text"
    question = "Can you generate a recipe based on the ingredients in this image?"
    training_data = "You are a chef. Please describe a detailed recipe using the ingredients you see in the image."
    image = request.files['image']

    # Prepare files for multipart upload
    files = {
        'images': (image.filename, image.stream, image.content_type)
    }

    # Prepare the payload
    payload = {
        "output_type": output_type,
        "question": question,
        "training_data": training_data,
        "stream_data": "false"
    }

    headers = {
        "Authorization": f"Bearer {API_KEY}"
    }

    url = "https://api.worqhat.com/api/ai/images/v2/image-analysis"
    try:
        response = requests.post(url, headers=headers, data=payload, files=files)
        response.raise_for_status()
        return response.text  # Return text response
    except requests.exceptions.RequestException as e:
        return str(e), 503

if __name__ == '__main__':
    app.run(debug=True)