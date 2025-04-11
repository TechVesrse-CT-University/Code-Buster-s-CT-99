# from flask import Flask, render_template, request, jsonify
# from gtts import gTTS
# import os
# import uuid
#
# app = Flask(__name__)
#
# @app.route("/")
# def home():
#     return render_template("index.html")
#
# @app.route("/get", methods=["POST"])
# def get_response():
#     user_msg = request.form.get("msg")
#
#     # Expanded intelligent responses
#     msg = user_msg.lower()
#     if "soil" in msg:
#         response = (
#             "Effective soil management starts with understanding your soil type and structure. "
#             "First, test the pH and nutrient levels through a soil test. Ideal pH for most crops ranges between 6.0 and 7.5. "
#             "Add organic matter like compost, cover crops, or manure to improve soil fertility and water retention. "
#             "Ensure proper drainage and avoid over-irrigation to prevent root rot. "
#             "Regular crop rotation can also improve soil health and reduce pest buildup."
#         )
#     elif "crop" in msg and "recommend" in msg:
#         response = (
#             "Crop recommendations depend on your region, soil type, and season. For loamy soils with moderate rainfall, "
#             "you can grow maize, soybean, groundnut, and vegetables like tomatoes and okra. "
#             "In arid regions, consider drought-tolerant crops like millets, sorghum, or pigeon pea. "
#             "Use crop rotation with legumes to fix nitrogen and improve soil fertility. "
#             "Also consider market demand, available irrigation, and pest resistance when selecting crops."
#         )
#     elif "disease" in msg:
#         response = (
#             "Crop diseases can range from fungal, bacterial, to viral infections. "
#             "For example, if you observe yellowing leaves and spots on tomato plants, it might be early blight or bacterial wilt. "
#             "To accurately diagnose, it's best to upload a clear image of the affected plant part. "
#             "Common treatments include neem oil sprays, copper-based fungicides, and crop rotation to avoid recurrence. "
#             "Also ensure proper spacing and sunlight to reduce humidity-related diseases."
#         )
#     elif "hello" in msg or "hi" in msg:
#         response = (
#             "Hello! I’m your Agri Assistant. 🌾 I'm here to help you with farming advice, crop recommendations, soil management, "
#             "and plant disease support. Just ask a question like 'What crop should I grow this season?' or 'How to improve my soil?'"
#         )
#     else:
#         response = (
#             "I'm here to support your agricultural needs. 🌱 You can ask me about:\n"
#             "- Soil health and improvement techniques\n"
#             "- Crop selection based on soil and climate\n"
#             "- Detecting and treating plant diseases\n"
#             "- Sustainable farming practices\n"
#             "Feel free to type a message like 'Recommend a crop for sandy soil' or 'How to treat leaf spot disease'."
#         )
#
#     # Generate speech
#     filename = f"{uuid.uuid4()}.mp3"
#     filepath = os.path.join("static", filename)
#     tts = gTTS(text=response, lang="en")
#     tts.save(filepath)
#
#     return jsonify({"response": response, "audio": filename})
#
# if __name__ == "__main__":
#     app.run(debug=True)

# from flask import Flask, render_template, request, jsonify
# from gtts import gTTS
# import os
# import uuid
#
# app = Flask(__name__)
#
# # --- Keyword-based Response Map ---
#
# response_map = [
#     {
#         "keywords": {"soil", "manage"},
#         "response": (
#             "To manage soil effectively, start with a soil test to determine pH and nutrient levels. "
#             "For most crops, a pH between 6.0 and 7.5 is ideal. Improve fertility by adding compost, cow dung, or green manure. "
#             "Cover crops like clover or rye can also increase organic matter. Minimize tillage to preserve structure and microbial life. "
#             "Practice crop rotation and avoid mono-cropping to reduce nutrient depletion and pests. Regularly monitor moisture levels and use mulching to retain water."
#         )
#     },
#     {
#         "keywords": {"crop", "recommend"},
#         "response": (
#             "Crop recommendation depends on your region, soil type, and climate. For example:\n"
#             "- In northern India with loamy soil: wheat, mustard, sugarcane\n"
#             "- In southern India: paddy, ragi, millets\n"
#             "- In dry areas: sorghum, bajra, pigeon pea\n"
#             "- For kitchen gardening: spinach, tomato, brinjal, coriander\n"
#             "Always rotate between legumes and cereals to balance soil nutrients and reduce pest buildup."
#         )
#     },
#     {
#         "keywords": {"disease", "detect"},
#         "response": (
#             "Plant disease detection often requires observing leaf spots, stem rot, or fungal growth. "
#             "You can take a clear image of the infected plant part and send it for expert review. "
#             "Common signs:\n- Yellow leaves: nutrient deficiency or blight\n- White powder: powdery mildew\n"
#             "- Dark spots: bacterial or fungal infection\n"
#             "Ensure good drainage, proper spacing, and use certified disease-free seeds. Natural remedies include neem oil and baking soda spray. "
#             "For severe cases, consult with your nearest Krishi Vigyan Kendra or agri extension officer."
#         )
#     },
#     {
#         "keywords": {"fertilizer", "use"},
#         "response": (
#             "Use fertilizers based on soil needs. Overuse can lead to toxicity. "
#             "Nitrogen (urea), Phosphorus (DAP), and Potassium (MOP) are major nutrients. Use organic options like vermicompost, cow dung, or poultry manure for better long-term results. "
#             "Split application of fertilizers (before planting and during crop growth) improves absorption. Always water the soil after applying fertilizer to avoid burning roots."
#         )
#     },
#     {
#         "keywords": {"pest", "control"},
#         "response": (
#             "Integrated Pest Management (IPM) is the best way to control pests. Start with biological control: use ladybugs or parasitoid wasps to control aphids. "
#             "Neem oil spray or garlic-chili sprays are great natural pesticides. For major infestations, use chemical sprays like chlorpyrifos or imidacloprid — but only in recommended quantities. "
#             "Keep the farm clean, avoid water stagnation, and inspect plants regularly to prevent outbreaks."
#         )
#     },
#     {
#         "keywords": {"irrigation", "method"},
#         "response": (
#             "Efficient irrigation improves yield and saves water. Use drip irrigation for crops like vegetables and fruit trees — it delivers water directly to roots. "
#             "Sprinkler irrigation is good for lawns and field crops. Flood irrigation is cheap but leads to water loss and root diseases. "
#             "Also try mulching and rainwater harvesting to conserve water. Water early in the morning or late evening to reduce evaporation losses."
#         )
#     },
#     {
#         "keywords": {"weather", "forecast"},
#         "response": (
#             "Checking weather forecasts helps in planning sowing, irrigation, and harvesting. For real-time updates, use IMD's weather app or apps like Mausam, Skymet, or AccuWeather. "
#             "Avoid sowing before rains or applying fertilizer before heavy storms. A cloudy, humid day may increase chances of fungal infections, so consider spraying neem or antifungal mixes beforehand."
#         )
#     },
#     {
#         "keywords": {"hi","hy"},
#         "response": (
#             "Hi there! 👋 I'm your friendly Agri Assistant. You can ask me about crops, soil, pests, fertilizers, and more. "
#             "Try something like 'Which crop should I grow after harvesting rice?' or 'How to treat leaf curl disease?'."
#         )
#     },
#     {
#         "keywords": {"hello","hlo"},
#         "response": (
#             "Hello farmer! 🌾 I'm your smart agri buddy. I can help with soil improvement, crop planning, disease diagnosis, and pest control. "
#             "Type your question and I’ll assist you the best I can!"
#         )
#     }
# ]
#
# default_response = (
#     "I'm here to support your farming queries 🌿. You can ask about:\n"
#     "- Soil health and how to improve it\n"
#     "- What crops to grow in your area\n"
#     "- Common pests or plant diseases\n"
#     "- Best irrigation and fertilizer practices\n"
#     "For example, try asking 'How to improve clay soil?' or 'Suggest a crop for dry season farming'."
# )
#
# # --- Match Function ---
# def match_response(message):
#     message_words = set(message.lower().split())
#     for item in response_map:
#         if item["keywords"].issubset(message_words):
#             return item["response"]
#     return default_response
#
#
# # --- Flask Routes ---
#
# @app.route("/")
# def home():
#     return render_template("index.html")
#
# @app.route("/get", methods=["POST"])
# def get_response():
#     user_msg = request.form.get("msg")
#     response = match_response(user_msg)
#
#     # Generate TTS audio
#     filename = f"{uuid.uuid4()}.mp3"
#     filepath = os.path.join("static", filename)
#     tts = gTTS(text=response, lang="en")
#     tts.save(filepath)
#
#     return jsonify({"response": response, "audio": filename})
#
#
# if __name__ == "__main__":
#     app.run(debug=True)
#
# from flask import Flask, render_template, request, jsonify
# from gtts import gTTS
# import os
# import uuid
#
# app = Flask(__name__)
#
#
# # Predefined responses in multiple languages
# response_map = {
#     "soil": {
#         "en": "To manage soil, start with a soil test, then add compost or organic matter.",
#         "hi": "मिट्टी का प्रबंधन करने के लिए पहले मिट्टी की जांच करें, फिर खाद या जैविक सामग्री मिलाएं।",
#         "pa": "ਮਿੱਟੀ ਦੀ ਸੰਭਾਲ ਲਈ ਮਿੱਟੀ ਦੀ ਜਾਂਚ ਕਰਵਾਓ ਅਤੇ ਕੱਚੀ ਖਾਦ ਜਾਂ ਜੈਵਿਕ ਪਦਾਰਥ ਪਾਓ।"
#     },
#     "crop recommend": {
#         "en": "Based on your region, I recommend maize, soybean, or groundnut.",
#         "hi": "आपके क्षेत्र के अनुसार मैं मक्का, सोयाबीन या मूंगफली की सिफारिश करता हूँ।",
#         "pa": "ਤੁਹਾਡੇ ਖੇਤਰ ਅਨੁਸਾਰ ਮੈਂ ਮੱਕੀ, ਸੋਯਾਬੀਨ ਜਾਂ ਮੂੰਗਫਲੀ ਦੀ ਸਿਫਾਰਿਸ਼ ਕਰਦਾ ਹਾਂ।"
#     },
#     "disease": {
#         "en": "Please upload an image for accurate disease detection. It may be fungal blight.",
#         "hi": "सटीक रोग पहचान के लिए कृपया एक छवि अपलोड करें। यह फफूंद जनित रोग हो सकता है।",
#         "pa": "ਸਹੀ ਬੀਮਾਰੀ ਦੀ ਪਛਾਣ ਲਈ ਕਿਰਪਾ ਕਰਕੇ ਇੱਕ ਚਿੱਤਰ ਅੱਪਲੋਡ ਕਰੋ। ਇਹ ਫਫੂੰਦ ਵਾਲੀ ਬੀਮਾਰੀ ਹੋ ਸਕਦੀ ਹੈ।"
#     },
#     "hello": {
#         "en": "Hello! I’m your Agri Assistant. Ask me about crops, soil, or plant health.",
#         "hi": "नमस्ते! मैं आपका कृषि सहायक हूँ। मुझसे फसल, मिट्टी या पौधों के स्वास्थ्य के बारे में पूछें।",
#         "pa": "ਸਤ ਸ੍ਰੀ ਅਕਾਲ! ਮੈਂ ਤੁਹਾਡਾ ਖੇਤੀਬਾੜੀ ਸਹਾਇਕ ਹਾਂ। ਮੈਨੂੰ ਫਸਲਾਂ, ਮਿੱਟੀ ਜਾਂ ਪੌਦਿਆਂ ਦੀ ਸਿਹਤ ਬਾਰੇ ਪੁੱਛੋ।"
#     },
#     "default": {
#         "en": "I'm here to help. Ask me about soil, crops, or diseases.",
#         "hi": "मैं आपकी मदद के लिए यहां हूं। मुझसे मिट्टी, फसल या रोगों के बारे में पूछें।",
#         "pa": "ਮੈਂ ਤੁਹਾਡੀ ਮਦਦ ਲਈ ਇੱਥੇ ਹਾਂ। ਮੈਨੂੰ ਮਿੱਟੀ, ਫਸਲਾਂ ਜਾਂ ਬੀਮਾਰੀਆਂ ਬਾਰੇ ਪੁੱਛੋ।"
#     }
# }
#
#
# def detect_intent(msg):
#     msg = msg.lower()
#     if "soil" in msg:
#         return "soil"
#     elif "crop" in msg and "recommend" in msg:
#         return "crop recommend"
#     elif "disease" in msg:
#         return "disease"
#     elif "hello" in msg or "hi" in msg:
#         return "hello"
#     else:
#         return "default"
#
#
# @app.route("/")
# def home():
#     return render_template("index.html")
#
#
# @app.route("/get", methods=["POST"])
# def get_response():
#     user_msg = request.form.get("msg")
#     lang = request.form.get("lang", "en")
#
#     intent = detect_intent(user_msg)
#     response = response_map.get(intent, response_map["default"]).get(lang, response_map["default"]["en"])
#
#     # Generate speech
#     filename = f"{uuid.uuid4()}.mp3"
#     filepath = os.path.join("static", filename)
#     tts = gTTS(text=response, lang=lang)
#     tts.save(filepath)
#
#     return jsonify({"response": response, "audio": filename})
#
#
# if __name__ == "__main__":
#     app.run(debug=True)
from flask import Flask, render_template, request, jsonify
from gtts import gTTS
import os
import uuid

app = Flask(__name__)

response_map = {
    "soil": {
        "en": "To manage soil, start with a soil test, then add compost or organic matter.",
        "hi": "मिट्टी का प्रबंधन करने के लिए पहले मिट्टी की जांच करें, फिर खाद या जैविक सामग्री मिलाएं।",
        "pa": "ਮਿੱਟੀ ਦੀ ਸੰਭਾਲ ਲਈ ਮਿੱਟੀ ਦੀ ਜਾਂਚ ਕਰਵਾਓ ਅਤੇ ਕੱਚੀ ਖਾਦ ਜਾਂ ਜੈਵਿਕ ਪਦਾਰਥ ਪਾਓ।",
        "fr": "Pour gérer le sol, commencez par un test, puis ajoutez du compost ou de la matière organique.",
        "ru": "Для управления почвой начните с анализа и добавьте компост или органику."
    },
    "crop recommend": {
        "en": "Based on your region, I recommend maize, soybean, or groundnut.",
        "hi": "आपके क्षेत्र के अनुसार मैं मक्का, सोयाबीन या मूंगफली की सिफारिश करता हूँ।",
        "pa": "ਤੁਹਾਡੇ ਖੇਤਰ ਅਨੁਸਾਰ ਮੈਂ ਮੱਕੀ, ਸੋਯਾਬੀਨ ਜਾਂ ਮੂੰਗਫਲੀ ਦੀ ਸਿਫਾਰਿਸ਼ ਕਰਦਾ ਹਾਂ।",
        "fr": "En fonction de votre région, je recommande le maïs, le soja ou l'arachide.",
        "ru": "В зависимости от вашего региона я рекомендую кукурузу, сою или арахис."
    },
    "disease": {
        "en": "Please upload an image for accurate disease detection. It may be fungal blight.",
        "hi": "सटीक रोग पहचान के लिए कृपया एक छवि अपलोड करें। यह फफूंद जनित रोग हो सकता है।",
        "pa": "ਸਹੀ ਬੀਮਾਰੀ ਦੀ ਪਛਾਣ ਲਈ ਕਿਰਪਾ ਕਰਕੇ ਇੱਕ ਚਿੱਤਰ ਅੱਪਲੋਡ ਕਰੋ। ਇਹ ਫਫੂੰਦ ਵਾਲੀ ਬੀਮਾਰੀ ਹੋ ਸਕਦੀ ਹੈ।",
        "fr": "Veuillez télécharger une image pour un diagnostic précis. Cela peut être une maladie fongique.",
        "ru": "Пожалуйста, загрузите изображение для точной диагностики. Это может быть грибковое заболевание."
    },
    "hello": {
        "en": "Hello! I’m your Agri Assistant. Ask me about crops, soil, or plant health.",
        "hi": "नमस्ते! मैं आपका कृषि सहायक हूँ। मुझसे फसल, मिट्टी या पौधों के स्वास्थ्य के बारे में पूछें।",
        "pa": "ਸਤ ਸ੍ਰੀ ਅਕਾਲ! ਮੈਂ ਤੁਹਾਡਾ ਖੇਤੀਬਾੜੀ ਸਹਾਇਕ ਹਾਂ। ਮੈਨੂੰ ਫਸਲਾਂ, ਮਿੱਟੀ ਜਾਂ ਪੌਦਿਆਂ ਦੀ ਸਿਹਤ ਬਾਰੇ ਪੁੱਛੋ।",
        "fr": "Bonjour ! Je suis votre assistant agricole. Demandez-moi sur les cultures ou la santé des plantes.",
        "ru": "Здравствуйте! Я ваш агроассистент. Спросите меня о почве, растениях или заболеваниях."
    },
    "default": {
        "en": "I'm here to help. Ask me about soil, crops, or diseases.",
        "hi": "मैं आपकी मदद के लिए यहां हूं। मुझसे मिट्टी, फसल या रोगों के बारे में पूछें।",
        "pa": "ਮੈਂ ਤੁਹਾਡੀ ਮਦਦ ਲਈ ਇੱਥੇ ਹਾਂ। ਮੈਨੂੰ ਮਿੱਟੀ, ਫਸਲਾਂ ਜਾਂ ਬੀਮਾਰੀਆਂ ਬਾਰੇ ਪੁੱਛੋ।",
        "fr": "Je suis là pour vous aider. Posez-moi des questions sur les sols ou les cultures.",
        "ru": "Я здесь, чтобы помочь. Спросите меня о почве, культурах или болезнях."
    }
}


def detect_intent(msg):
    msg = msg.lower()

    keywords = {
        "soil": ["soil", "मिट्टी", "ਮਿੱਟੀ"],
        "crop recommend": ["crop", "recommend", "फसल", "सिफारिश", "ਫਸਲ", "ਸਿਫਾਰਿਸ਼"],
        "disease": ["disease", "रोग", "ਬੀਮਾਰੀ", "बीमारी"],
        "hello": ["hello", "hi", "नमस्ते", "ਸਤ ਸ੍ਰੀ ਅਕਾਲ", "ਹੈਲੋ", "bonjour", "здравствуйте"]
    }

    for intent, words in keywords.items():
        if any(word in msg for word in words):
            return intent

    return "default"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get", methods=["POST"])
def get_response():
    user_msg = request.form.get("msg")
    lang = request.form.get("lang", "en")

    intent = detect_intent(user_msg)
    response = response_map.get(intent, response_map["default"]).get(lang, response_map["default"]["en"])

    filename = f"{uuid.uuid4()}.mp3"
    filepath = os.path.join("static", filename)
    tts = gTTS(text=response, lang=lang)
    tts.save(filepath)

    return jsonify({"response": response, "audio": filename})


if __name__ == "__main__":
    if not os.path.exists("static"):
        os.makedirs("static")
    app.run(debug=True)


