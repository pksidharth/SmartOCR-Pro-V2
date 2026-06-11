import cv2
import pytesseract
import os

if os.name == "nt":
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def simple_ocr(image_path):

    img = cv2.imread(image_path)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    _, processed = cv2.threshold(
        gray,
        150,
        255,
        cv2.THRESH_BINARY
    )

    text = pytesseract.image_to_string(processed)

    return text


def advanced_ocr(image_path):

    img = cv2.imread(image_path)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    blur = cv2.GaussianBlur(gray, (3, 3), 0)

    _, processed = cv2.threshold(
        blur,
        0,
        255,
        cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )

    text = pytesseract.image_to_string(processed)

    return text


def choose_pipeline(image_path):

    img = cv2.imread(image_path)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    if gray.std() > 50:
        print("Using SIMPLE pipeline")
        return simple_ocr(image_path)

    else:
        print("Using ADVANCED pipeline")
        return advanced_ocr(image_path)