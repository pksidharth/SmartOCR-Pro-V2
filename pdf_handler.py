import fitz
import os
from ocr import choose_pipeline


def extract_pdf_text(pdf_path):

    pdf = fitz.open(pdf_path)

    all_text = ""

    for page_number in range(len(pdf)):

        page = pdf[page_number]

        pix = page.get_pixmap()

        image_path = f"page_{page_number}.png"

        pix.save(image_path)

        page_text = choose_pipeline(image_path)

        all_text += f"\n\n----- PAGE {page_number + 1} -----\n\n"

        all_text += page_text

        if os.path.exists(image_path):
            os.remove(image_path)

    pdf.close()

    return all_text