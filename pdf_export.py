from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont


pdfmetrics.registerFont(
    TTFont(
        "Malayalam",
        "fonts/NotoSansMalayalam.ttf"
    )
)


def create_pdf(text, filename):

    pdf = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    styles["BodyText"].fontName = "Malayalam"

    content = []

    for line in text.split("\n"):

        content.append(
            Paragraph(
                line,
                styles["BodyText"]
            )
        )

    pdf.build(content)

    return filename