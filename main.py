"""
FELIPEDELOSH - 2024

WARNING: you need install:


Enter a PDF files in folder: PDF
"""
from os import scandir # To read all files in folder
# Python -m pip install PyMuPDF 
import fitz # To read PDF text

# Configurations vars
_PDF_FOLDER_PATH = "PDF"


# READ ALL FILES IN PDF FOLDER and save filename
_PDF_FILES_PATH = []

for i in scandir(_PDF_FOLDER_PATH):
    if i.is_file():
        if "pdf" in i.name:
            _PDF_FILES_PATH.append(i.name)


# Save all text content in PDF files

for i in _PDF_FILES_PATH:
    _iterPdfPath = f"{_PDF_FOLDER_PATH}/{i}"
    document = fitz.open(_iterPdfPath)
    # Read all Text
    for num_page in range(document.page_count):
        pdf_page = document[num_page]
        txt = pdf_page.get_text()
        print(txt)
