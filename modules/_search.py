import streamlit as st

from keyword_search import search_keyword


def show_search():

    st.title("🔍 Keyword Search")

    if "ocr_text" not in st.session_state:

        st.warning(
            "Please extract OCR text first."
        )

        return

    keyword = st.text_input(
        "Enter Keyword"
    )

    if st.button(
        "Search"
    ):

        matches = search_keyword(
            st.session_state["ocr_text"],
            keyword
        )

        st.success(
            f"Keyword found {len(matches)} time(s)"
        )

        if len(matches) > 0:

            st.subheader(
                "Matching Lines"
            )

            for line in matches:

                st.write(
                    "•", line
                )

        else:

            st.warning(
                "Keyword not found"
            )