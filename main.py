import PyPDF2
import requests

with open('Lorem_ipsum.pdf', 'rb') as pdffile:
    pdfReader = PyPDF2.PdfReader(pdffile)
    print(pdfReader.pages[0].extract_text())
