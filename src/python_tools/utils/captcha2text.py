from subprocess import check_output
from PIL import Image
from pytesseract import image_to_string


def resolve_captcha(path):
    check_output(['convert', path, '-resample', '600', path])
    text_data = image_to_string(Image.open(path))
    return text_data.replace(" ", "").strip()
