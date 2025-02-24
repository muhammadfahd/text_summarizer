import streamlit as st
from openai import OpenAI

# Initialize OpenAI client
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="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",
)

def summarize_text(text):
    """Generates a concise summary of the given text."""
    if not text.strip():
        return "Please enter some text to summarize."

    completion = client.chat.completions.create(
        extra_headers={
            "HTTP-Referer": "<YOUR_SITE_URL>",  # Optional for rankings
            "X-Title": "<YOUR_SITE_NAME>",  # Optional for rankings
        },
        model="deepseek/deepseek-r1-distill-llama-70b:free",
        messages=[
            {"role": "system", "content": "You are an AI that summarizes text concisely."},
            {"role": "user", "content": f"Summarize the following text:\n{text}"}
        ]
    )
    return completion.choices[0].message.content

# Streamlit UI
st.set_page_config(page_title="AI Text Summarizer", page_icon="📝", layout="centered")

# Custom Styling
st.markdown("""
    <style>
    body {
        background-color: #f5f7fa;
    }
    .stApp {
        background-color: white;
        border-radius: 15px;
        padding: 20px;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
    }
    .title {
        font-size: 36px;
        font-weight: bold;
        text-align: center;
        color: #333;
    }
    .summary-box {
        background-color: #eef2f7;
        padding: 15px;
        border-radius: 10px;
        font-size: 18px;
        color: #333;
        box-shadow: inset 0 0 5px rgba(0, 0, 0, 0.1);
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<p class="title">📄 AI Text Summarizer</p>', unsafe_allow_html=True)
st.write("Enter your text below and get a concise summary instantly.")

# User Input
text_input = st.text_area("Enter your text here:", height=200, placeholder="Paste or type your text...")

# Summarize Button
if st.button("Summarize", use_container_width=True):
    with st.spinner("Generating summary... ⏳"):
        summary = summarize_text(text_input)
        st.markdown('<p class="summary-box">✍️ <b>Summary:</b></p>', unsafe_allow_html=True)
        st.success(summary)
