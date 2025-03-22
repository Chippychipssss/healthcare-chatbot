import google.generativeai as genai

genai.configure(api_key="AIzaSyDW8YtnSJRglYIi67CUjrQ04q4ObIlgv9M")  # Replace with your actual API key

models = genai.list_models()
for model in models:
    print(model.name)
