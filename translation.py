
import time
from deep_translator import GoogleTranslator
from deep_translator.exceptions import TooManyRequests


def translate_text(text, target_language):
    if not text or not text.strip():
        return ""

    translator = GoogleTranslator(
        source="auto",
        target=target_language
    )

    # Split long OCR text into manageable chunks.
    max_chars = 3500
    chunks = []

    remaining = text.strip()

    while remaining:
        if len(remaining) <= max_chars:
            chunks.append(remaining)
            break

        split_at = remaining.rfind(" ", 0, max_chars)

        if split_at <= 0:
            split_at = max_chars

        chunks.append(remaining[:split_at])
        remaining = remaining[split_at:].strip()

    translated_chunks = []

    for index, chunk in enumerate(chunks):
        if index > 0:
            time.sleep(1.2)

        translated_chunks.append(
            translator.translate(chunk)
        )

    return "\n".join(translated_chunks)
