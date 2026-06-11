import streamlit as st

from pdf_export import create_pdf


def show_export():

    st.title("📥 Export Center")

    if "ocr_text" in st.session_state:

        st.subheader(
            "📄 OCR Text Export"
        )

        st.download_button(
            label="Download OCR TXT",
            data=st.session_state["ocr_text"],
            file_name="ocr_output.txt",
            mime="text/plain"
        )

        pdf_file = create_pdf(
            st.session_state["ocr_text"],
            "ocr_output.pdf"
        )

        with open(
            pdf_file,
            "rb"
        ) as file:

            st.download_button(
                label="Download OCR PDF",
                data=file,
                file_name="ocr_output.pdf",
                mime="application/pdf"
            )

    else:

        st.warning(
            "No OCR text available."
        )

    st.divider()

    if "translated_text" in st.session_state:

        st.subheader(
            "🌍 Translated Text Export"
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

        with open(
            pdf_file,
            "rb"
        ) as file:

            st.download_button(
                label="Download Translation PDF",
                data=file,
                file_name="translated_output.pdf",
                mime="application/pdf"
            )

    else:

        st.warning(
            "No translated text available."
        )