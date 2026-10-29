
import streamlit as st

from translation import translate_text
from pdf_export import create_pdf


def show_translation():

    st.title("🌍 Translation")

    if "ocr_text" not in st.session_state:
        st.warning("Please extract OCR text first.")
        return

    st.subheader("Source Text")

    st.text_area(
        "OCR Text",
        st.session_state["ocr_text"],
        height=250
    )

    language = st.selectbox(
        "Select Language",
        ["en", "hi", "kn", "ml", "ta"]
    )

    if st.button("Translate Text"):
        try:
            with st.spinner("Translating..."):
                translated_text = translate_text(
                    st.session_state["ocr_text"],
                    language
                )

            st.session_state["translated_text"] = translated_text
            st.success("Translation completed!")

        except Exception as error:
            st.error(
                "Translation failed. Google Translate may be "
                "temporarily rate-limiting requests. Please wait "
                "and try again later."
            )
            st.caption(f"Details: {error}")

    if "translated_text" in st.session_state:

        st.subheader("Translated Text")

        st.text_area(
            "Translation",
            st.session_state["translated_text"],
            height=300
        )

        st.download_button(
            label="Download Translation TXT",
            data=st.session_state["translated_text"],
            file_name="translated_output.txt",
            mime="text/plain"
        )

        pdf_file = create_pdf(
            st.session_state["translated_text"],
            "translated_output.pdf"
        )

        with open(pdf_file, "rb") as file:
            st.download_button(
                label="Download Translation PDF",
                data=file,
                file_name="translated_output.pdf",
                mime="application/pdf"
            )
