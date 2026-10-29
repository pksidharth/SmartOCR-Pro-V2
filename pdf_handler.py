
import os
import shutil
import tempfile

from pdf2image import convert_from_path
from ocr import choose_pipeline


# Use a configured Poppler path if provided.
# Otherwise, use your local Windows installation if it exists.
POPPLER_PATH = os.environ.get("POPPLER_PATH")

LOCAL_POPPLER_PATH = (
    r"D:\BCA Project\poppler-26.09.0\Library\bin"
)

if not POPPLER_PATH and os.path.isdir(LOCAL_POPPLER_PATH):
    POPPLER_PATH = LOCAL_POPPLER_PATH

# On Linux/cloud, Poppler can be found through the system PATH.
if not POPPLER_PATH and shutil.which("pdftoppm"):
    POPPLER_PATH = None


def extract_pdf_text(pdf_path):
    all_text = ""

    pages = convert_from_path(
        pdf_path,
        poppler_path=POPPLER_PATH,
        dpi=200
    )

    for page_number, page_image in enumerate(pages):
        image_path = None

        try:
            with tempfile.NamedTemporaryFile(
                suffix=".png", delete=False
            ) as temp_file:
                image_path = temp_file.name

            page_image.save(image_path, format="PNG")
            page_text = choose_pipeline(image_path)

            all_text += (
                f"\n\n----- PAGE {page_number + 1} -----\n\n"
                + page_text
            )

        finally:
            if image_path and os.path.exists(image_path):
                os.remove(image_path)

            page_image.close()

    return all_text
