import streamlit as st


def show_home():

    st.title("📄 SmartOCR Pro")

    st.markdown("""
    ### AI Powered Document Digitization System

    Extract text from images and PDFs, translate content,
    search keywords and export documents with ease.
    """)

    st.divider()

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "OCR Engine",
            "Ready"
        )

    with col2:
        st.metric(
            "Languages",
            "5+"
        )

    with col3:
        st.metric(
            "Search",
            "Enabled"
        )

    with col4:
        st.metric(
            "Export",
            "TXT / PDF"
        )

    st.divider()

    st.subheader("🚀 Core Features")

    c1, c2 = st.columns(2)

    with c1:

        st.info("""
📤 OCR Extraction

• Image OCR

• PDF OCR

• Text Digitization
        """)

        st.info("""
🌍 Translation

• English

• Hindi

• Kannada

• Malayalam

• Tamil
        """)

    with c2:

        st.info("""
🔍 Keyword Search

• Fast Search

• Match Detection

• Line Results
        """)

        st.info("""
📥 Export

• TXT Download

• PDF Download

• Translation Export
        """)

    