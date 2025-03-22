import google.generativeai as genai

# 🔴 Replace this with your actual API key
API_KEY = "AIzaSyDW8YtnSJRglYIi67CUjrQ04q4ObIlgv9M"

# Configure API
def configure_api():
    if not API_KEY:
        raise ValueError("API Key is missing. Please add your API key.")
    
    genai.configure(api_key=API_KEY)
    print("✅ API configured successfully.")

# Initialize Models
def create_models():
    txt_model = genai.GenerativeModel('gemini-1.5-pro-latest')  # Best for text generation
    vis_model = genai.GenerativeModel('gemini-1.0-pro-vision-latest')  # Best for vision tasks
    return txt_model, vis_model

# Run Configuration
configure_api()

# Load models
txt_model, vis_model = create_models()
print("✅ Models initialized successfully.")
