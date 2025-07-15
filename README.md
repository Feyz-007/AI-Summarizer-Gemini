# 📚 Gemini AI PDF/Text Summarizer

An intelligent and customizable AI summarization tool built with Google's Gemini LLM and Streamlit.

---

## 📽️ Demo Video

🎬 [Watch on YouTube](https://youtu.be/Ptd5jAmlJAk)
---

## ✨ Features

- 📝 Summarize PDFs or pasted text  
- ⚙️ Customize prompts  
- 📄 View and download summaries  
- 🛡️ Automatically trims input beyond 6000 characters  
- 🧠 Powered by `gemini-1.5-flash-latest` via Gemini API  

---

## 🧠 How It Works

- Users provide input via text or PDF  
- A prompt (optional) controls how Gemini summarizes  
- Gemini returns a structured response (e.g., bullets or paragraphs)  
- Summary is displayed and available for download  

---

## 🚀 How to Run the App Locally

```bash
git clone https://github.com/Feyz-007/AI-Summarizer-Gemini.git 
cd AI-Summarizer-Gemini

# (Optional) Set up a virtual environment
python -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate         # Windows

# Install dependencies
pip install -r requirements.txt
```

---

## 🔐 Gemini API Setup

Get your API key from: [https://aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey)

Then, create a `.env` file in the root directory with this content:

```env
GEMINI_API_KEY=your_actual_gemini_api_key_here
```
---

## ▶️ To Run the App

```bash
streamlit run app.py
```

---

## 📂 Project Structure

```
ai-summarizer/
├── app.py
├── summarizer.py
├── utils.py
├── requirements.txt
├── .env.example
└── README.md
```

## 🧠 Evaluation Criteria:

### LLM Prompt Design & Chain of Reasoning:
Prompts are dynamically injected and fully customizable by the user. This allows Gemini to generate context-aware, structured summaries — whether in bullet points, paragraphs, or hybrid formats — depending on the user’s intent.

### UI & Output Clarity:
The interface is clean and intuitive, supporting both text and PDF inputs,Real-time input length display, and downloadable output summaries.

### Real-World Utility:
The tool is suitable for students, researchers, and content reviewers needing concise yet informative summaries from large documents.

