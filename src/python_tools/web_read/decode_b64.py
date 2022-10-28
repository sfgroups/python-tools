from bs4 import BeautifulSoup
import base64
from pathlib import Path

from bs4 import BeautifulSoup


def parse_html_file():
    download_folder = Path(Path.home(), 'Downloads', 'Test')
    html_filename = Path(download_folder, 'fmb.html')
    with open(html_filename, 'r') as f:
        contents = f.read()
        soup = BeautifulSoup(contents, 'lxml')
        pdftext = soup.find("embed").attrs['src']
        pdftext = pdftext.replace('data:application/pdf;base64,', '')

        return pdftext


def decode_b64():
    b64 = parse_html_file()

    with open(Path(Path.home(), 'Downloads', 'mytest.pdf'), "wb") as f:
        f.write(base64.b64decode(b64, validate=False))


def encode_64(filename):
    with open(filename, "rb") as pdf_file:
        encoded_string = base64.b64encode(pdf_file.read())
        print(encoded_string)


if __name__ == "__main__":
    decode_b64()
