import os, requests, json, time
import PyPDF2
from dotenv import load_dotenv

load_dotenv()

# Extract text from pdf
with open("Lorem_ipsum.pdf", "rb") as pdffile:
    pdfReader = PyPDF2.PdfReader(pdffile)
    pdf_text = pdfReader.pages[0].extract_text()


# Create Text-to-Speech job
url = "https://large-text-to-speech.p.rapidapi.com/tts"

payload = {"text": pdf_text}
headers = {
    "content-type": "application/json",
    "X-RapidAPI-Key": os.getenv("X-RapidAPI-Key"),
    "X-RapidAPI-Host": "large-text-to-speech.p.rapidapi.com",
}

response1 = requests.request("POST", url, json=payload, headers=headers)
filename = "test-file.wav"
job_id = json.loads(response1.text)["id"]
eta = json.loads(response1.text)["eta"]
print(f"Waiting {eta} seconds for the job to finish...")
time.sleep(eta * 2)
response = requests.request(
    "GET",
    "https://large-text-to-speech.p.rapidapi.com/tts",
    headers=headers,
    params={"id": job_id},
)

while "url" not in json.loads(response.text):
    response = requests.request(
        "GET",
        "https://large-text-to-speech.p.rapidapi.com/tts",
        headers=headers,
        params={"id": job_id},
    )
    print(f"Waiting some more...")
    time.sleep(3)

url = json.loads(response.text)['url']
response = requests.request("GET", url)

with open(filename, "wb") as f:
    f.write(response.content)
print(f"File saved to {filename} ! \nOr download here: {url}")
