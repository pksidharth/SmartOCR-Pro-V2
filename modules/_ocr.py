import streamlit as st
import tempfile

from ocr import choose_pipeline
from pdf_handler import extract_pdf_text


def show_ocr():

    st.title("📤 OCR Extraction")

    uploaded_file = st.file_uploader(
        "Choose a file",
        type=["png", "jpg", "jpeg", "pdf"]
    )

    if uploaded_file is not None:

        file_name = uploaded_file.name.lower()

        col1, col2 = st.columns(2)

        with col1:

            if file_name.endswith(".pdf"):

                st.success("PDF Uploaded")

            else:

                st.image(
                    uploaded_file,
                    caption="Uploaded Image"
                )

        with col2:

            if st.button("Extract Text"):

                with st.spinner(
                    "Running OCR..."
                ):

                    if file_name.endswith(".pdf"):

                        with tempfile.NamedTemporaryFile(
                            delete=False,
                            suffix=".pdf"
                        ) as tmp_file:

                            tmp_file.write(
                                uploaded_file.read()
                            )

                            temp_path = tmp_file.name

                        extracted_text = (
                            extract_pdf_text(
                                temp_path
                            )
                        )

                    else:

                        with tempfile.NamedTemporaryFile(
                            delete=False,
                            suffix=".png"
                        ) as tmp_file:

                            tmp_file.write(
                                uploaded_file.read()
                            )

                            temp_path = tmp_file.name

                        extracted_text = (
                            choose_pipeline(
                                temp_path
                            )
                        )

                    st.session_state[
                        "ocr_text"
                    ] = extracted_text

    if "ocr_text" in st.session_state:

        st.subheader(
            "📄 OCR Output"
        )

        st.caption(
            "Extracted text from uploaded document"
        )
        st.text_area(
            "Extracted Text",
            st.session_state["ocr_text"],
            height=350
        )

        words = len(
            st.session_state[
                "ocr_text"
            ].split()
        )

        chars = len(
            st.session_state[
                "ocr_text"
            ]
        )

        lines = len(
            st.session_state[
                "ocr_text"
            ].splitlines()
        )

        c1, c2, c3 = st.columns(3)

        c1.metric(
            "Words",
            words
        )

        c2.metric(
            "Characters",
            chars
        )

        c3.metric(
            "Lines",
            lines
        )