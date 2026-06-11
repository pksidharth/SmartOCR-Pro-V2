import streamlit as st

st.set_page_config(
    page_title="SmartOCR Pro",
    page_icon="📄",
    layout="wide"
)

st.markdown("""
<style>

.stApp {
    background-color: #0f172a;
}

</style>
""", unsafe_allow_html=True)

st.sidebar.title("📄 SmartOCR Pro")

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Home",
        "📤 OCR",
        "🌍 Translation",
        "🔍 Search",
        "📥 Export",
        "ℹ About"
    ]
)

if page == "🏠 Home":

    from modules._home import show_home
    show_home()

elif page == "📤 OCR":

    from modules._ocr import show_ocr
    show_ocr()

elif page == "🌍 Translation":

    from modules._translation_page import show_translation
    show_translation()

elif page == "🔍 Search":

    from modules._search import show_search
    show_search()

elif page == "📥 Export":

    from modules._export import show_export
    show_export()

elif page == "ℹ About":

    from modules._about import show_about
    show_about()