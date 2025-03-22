from PIL import Image
def generate_response(history, text, img, txt_model, vis_model, default_prompt="You are FALCON AI, falcon Health Care Chatbot chatbot. Answer only as a Health Expert, decline anything outside this domain."):
    try:
        if img:
            img = Image.open(img)
            response = vis_model.generate_content([text,default_prompt, img])
            history.append((None, response.text))
        else:
            response = txt_model.generate_content([text, default_prompt])
            history.append((None, response.text))
        print("Response generated successfully.")
        return history
    except Exception as e:
        error_msg = f"Error processing your input: {str(e)}"
        print(error_msg)
        return [(error_msg, None)]
