import streamlit as st


def show_about():

    st.title("ℹ About SmartOCR Pro")

    st.markdown("""
    ### 📄 Project Information

    **Project Name:**

    SmartOCR Pro

    **Course:**

    Bachelor of Computer Applications (BCA)

    **Description:**

    SmartOCR Pro is a document digitization system that extracts text from images and PDFs using OCR technology. The system supports text extraction, multilingual translation, keyword searching, and export functionality.

    ---

    ### 👨‍💻 Developers

    1. Sidharth P.K

    2. Muhammed Aadil M.C

    3. Aldrin Shaji

    ---

    ### 🛠 Technologies Used

    - Python
    - Streamlit
    - OpenCV
    - Tesseract OCR
    - PyMuPDF
    - Deep Translator
    - ReportLab

    ---

    ### 🚀 Features

    ✅ OCR Text Extraction

    ✅ PDF OCR Processing

    ✅ Multi-Language Translation

    ✅ Keyword Search

    ✅ TXT Export

    ✅ PDF Export

    ✅ Modern Dashboard Interface

    ---

    ### 🎯 Project Objective

    To convert scanned documents, images, and PDFs into editable digital text while providing translation, search, and export capabilities through a user-friendly interface.
    """)

    st.success("SmartOCR Pro Version 2.0")

    st.info("Developed as a BCA Mini Project")