import streamlit as st
from utils.ocr_utils import extract_text_from_image
from utils.gemini_utils import analyze_report_with_gemini
from PIL import Image
import io

st.set_page_config(page_title="Medical Report Analyzer", layout="wide")

st.title("🩺 Medical Report Analyzer")
st.markdown("Upload your medical report (image or PDF), and let AI analyze and summarize it.")

uploaded_file = st.file_uploader("Upload Medical Report", type=["png", "jpg", "jpeg", "pdf"])

if uploaded_file:
    if uploaded_file.type == "application/pdf":
        from utils.pdf_utils import pdf_to_images
        images = pdf_to_images(uploaded_file)
    else:
        images = [Image.open(uploaded_file)]

    full_text = ""
    for img in images:
        st.image(img, caption="Uploaded Page", use_column_width=True)
        text = extract_text_from_image(img)
        full_text += text + "\n\n"

    with st.expander("🔍 Extracted Text"):
        st.text_area("Raw OCR Output", full_text, height=300)

    if st.button("Analyze with Gemini"):
        with st.spinner("Analyzing..."):
            report_summary = analyze_report_with_gemini(full_text)
            st.success("Analysis Complete ✅")
            st.markdown(report_summary)
