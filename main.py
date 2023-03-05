import os, requests, json, time
import PyPDF2
from dotenv import load_dotenv

load_dotenv()

# Extract text from pdf
with open('Lorem_ipsum.pdf', 'rb') as pdffile:
    pdfReader = PyPDF2.PdfReader(pdffile)
    pdf_text = pdfReader.pages[0].extract_text()


# Create Text-to-Speech job
url = "https://large-text-to-speech.p.rapidapi.com/tts"

payload = {"text": pdf_text}
headers = {
    "content-type": "application/json",
    "X-RapidAPI-Key": os.getenv('X-RapidAPI-Key'),
    "X-RapidAPI-Host": "large-text-to-speech.p.rapidapi.com"
}

response = requests.request("POST", url, json=payload, headers=headers)

print(response.text)
