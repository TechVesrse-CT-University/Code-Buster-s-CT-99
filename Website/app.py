from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import os

app = Flask(__name__)

# Configure Gemini API
genai.configure(api_key="YOUR_API_KEY")  # Replace with your actual key

generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
)

def GenerateResponse(input_text):
    prompt = [
       "you are a fashion and styling recommender chatbot so reply accordingly.",
       f"input:{input_text}",
       "output:"
    ]
    response = model.generate_content(prompt)
    return response.text

# ROUTES

@app.route('/')
def home():
    return render_template('index.html')  # Home page

@app.route('/crop-selection')
def crop_selection():
    return render_template('crop-selection.html')

@app.route('/soil-management')
def soil_management():
    return render_template('soil-management.html')

@app.route('/disease-detection')
def disease_detection():
    return render_template('disease-detection.html')

@app.route('/community')
def community():
    return render_template('community.html')

@app.route('/about')
def about():
    return render_template('about.html')

# Chatbot API
@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_input = data.get('message', '')
    reply = GenerateResponse(user_input)
    return jsonify({'response': reply})


if __name__ == '__main__':
    app.run(debug=True)
