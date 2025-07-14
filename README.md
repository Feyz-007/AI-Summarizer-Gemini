
# 📚 Gemini AI PDF/Text Summarizer

An intelligent and customizable AI summarization tool built with **Google's Gemini LLM** and **Streamlit**.

---

## ✨ Features

- 📝 Summarize PDFs or pasted text
- ⚙️ Customize prompts
- 📄 View and download summaries
- 🛡️ Automatically trims input beyond 6000 characters
- 🧠 Powered by `gemini-1.5-flash-latest` via Gemini API

---

## 🧠 How It Works

-Users provide input via text or PDF
-A prompt (optional) controls how Gemini summarizes
-Gemini returns a structured response (e.g., bullets or paragraphs)
-Summary is displayed and available for download

---

## 🚀 How to Run the App Locally

```bash
git clone https://github.com/Feyz-007/AI-Summarizer-Gemini-.git
cd ai-summarizer-gemini

```
###optional
```bash
python -m venv venv
source venv/bin/activate      # macOS/Linux
venv\Scripts\activate       # Windows
```
```bash
pip install -r requirements.txt
```

### **Add your Gemini API key**

🔐 Gemini API Setup
Get your API key from: https://aistudio.google.com/app/apikey

Create a `.env` file in the root directory with the following:

```env
GEMINI_API_KEY=your_actual_gemini_api_key_here
```
---
### **Add your Gemini API key**

To run:

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