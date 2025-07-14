import streamlit as st
from utils import extract_text_from_pdf
from summarizer import summarize_full_text

st.set_page_config(page_title="📚 Gemini AI Summarizer", layout="centered")

# Title and description
st.markdown("## 📚 AI Summarizer with Gemini LLM")
st.markdown("Summarize long documents or text using Gemini — with structured, readable, and customizable outputs.")
st.markdown("---")

# Input type
input_type = st.radio("Choose input type:", ("Upload PDF", "Enter Text"), horizontal=True)
text = ""

if input_type == "Upload PDF":
    uploaded_file = st.file_uploader("📎 Upload a PDF", type="pdf")
    if uploaded_file:
        with st.spinner("📖 Extracting text..."):
            text = extract_text_from_pdf(uploaded_file)
            st.success("✅ Text extracted.")
            st.text_area("Text Preview", text[:3000], height=200)
else:
    text = st.text_area("✍️ Enter text to summarize:", height=300, placeholder="Paste or write your article here...")

# Show character count
if text:
    st.caption(f"🧾 Input Length: {len(text)} characters")

# Character limit enforcement
MAX_CHARS = 6000
if len(text) > MAX_CHARS:
    st.warning(f"⚠️ Input too long. Only the first {MAX_CHARS:,} characters will be processed.")
    text = text[:MAX_CHARS]


# Custom prompt
st.markdown("### ⚙️ Custom Prompt")
with st.expander("✏️ Customize Gemini Instructions (optional)", expanded=False):
    st.caption(" Use this to shape Gemini’s behavior. Example — 'List key ideas as bullet points' or 'Summarize for a beginner.'")
    custom_prompt = st.text_area(
        "Your custom instruction:",
        placeholder="E.g., 'Summarize each section in 2 lines' or 'Highlight only the advantages in bullet form'",
        height=100
    )


# Summarize button
if text and st.button("🚀 Summarize Now"):
    with st.spinner("🧠 Summarizing with Gemini..."):
        summary = summarize_full_text(text, custom_prompt)
        st.success("✅ Summary generated successfully!")

    # Final output
    st.markdown("### 📌 Final Summary")
    st.markdown(summary)

    st.download_button(
        label="💾 Download Summary as .txt",
        data=summary,
        file_name="summary.txt",
        mime="text/plain"
    )
