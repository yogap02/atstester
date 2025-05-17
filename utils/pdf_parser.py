from dotenv import load_dotenv
import pymupdf
import sys
import os

load_dotenv()
DEBUG = os.getenv("DEBUG", "false").lower() == "true"

def read_docs(file):
    doc = pymupdf.open(file)
    text = ""
    for page in doc:
        text += page.get_text()
    if DEBUG: print (text)
    return text

def detect_images(file_path):
    doc = pymupdf.open(file_path)
    count = 0
    for page in doc:
        count += len(page.get_images(full=True))
    if DEBUG: print (count)
    return count