"""
python 3.11.2, sys 3.11.2, PyPDF2 3.0.1, py-anki 0.0.6, opencv-python 4.7.0.72
"""

import sys
from PyPDF2 import PdfReader
from py_anki import AnkiApi
import cv2


def input_path():
    path = input("Укажите путь до PDF файла: ")
    path = "Magaziny_vokabulyar.pdf"
    return path


def read_pdf(path):
    reader = PdfReader(path)
    page = reader.pages[0]
    print(page.extract_text())


if __name__ == "__main__":
    path = input_path()
    read_pdf(path)
