# Recipe Generator

## Overview
The Recipe Generator is a web application that generates a recipe based on the ingredients detected in an uploaded image. This application uses a Flask backend to handle the image upload and communicate with an external API for image analysis.

## Features
- Upload an image containing food ingredients.
- Receive a detailed recipe based on the detected ingredients.
- Responsive design with a visually appealing interface.

## Technologies Used
- Flask: Backend framework
- HTML/CSS: Frontend design
- Requests: To handle API calls
- External API: For image analysis and recipe generation

## Prerequisites
Before you begin, ensure you have met the following requirements:
- Python 3.6+
- Flask
- Requests library
- API key for the external image analysis service

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/Recipe-Generator-using-flask.git
   cd Recipe-Generator-using-flask
   ```

2. **Set up a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set your API key:**
   Replace the placeholder `API_KEY` with your actual API key in the `app.py` file.

## Usage

1. **Run the Flask application:**
   ```bash
   python app.py
   ```

2. **Open your browser and navigate to:**
   ```
   http://127.0.0.1:5000
   ```

3. **Upload an image:**
   - Choose an image containing food ingredients.
   - Click the "Generate Recipe" button.

4. **View the generated recipe:**
   - The application will display the recipe based on the ingredients detected in the uploaded image.

## Project Structure

```
recipe-generator/
│
├── static/
│   ├── styles.css       # CSS file for styling the frontend
│
├── templates/
│   ├── index.html       # HTML template for the main page
│
├── app.py               # Main Flask application file
├── requirements.txt     # List of dependencies
└── README.md            # This README file
```

## API Configuration

The application uses an external API for image analysis and recipe generation. Ensure you have a valid API key and replace the placeholder in the `app.py` file:

```python
API_KEY = "your_actual_api_key_here"
```


## License

This project is licensed under the MIT License. Feel free to modify and use the code as per your needs.
