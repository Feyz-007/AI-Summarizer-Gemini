import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("models/gemini-1.5-flash-latest")

def summarize_full_text(text, custom_prompt=None):
    # Default prompt
    if not custom_prompt or custom_prompt.strip() == "":
        prompt = (
            "Summarize the following content clearly and informatively:\n"
            "- Start with a short paragraph overview.\n"
            "- Use bullet points or short paragraphs to explain key sections if there is large contents present.\n"
            "- Preserve the structure and key details without adding anything new.\n"
            ""
        )
    else:
        prompt = custom_prompt.strip()

    full_input = f"{prompt}\n\n{text}"

    try:
        response = model.generate_content(full_input)
        return response.text.strip()
    except Exception as e:
        if "429" in str(e):
            return "⚠️ Quota exceeded. Please try again later or use a new API key."
        return f"⚠️ Error: {str(e)}"
