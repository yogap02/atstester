from dotenv import load_dotenv
import pymupdf
import os

# Fetch environment variables from .env to set DEBUG
load_dotenv()
DEBUG = os.getenv("DEBUG", "false").lower() == "true"

# utility functions to read PDF documents
def read_docs(file):
    doc = pymupdf.open(file)
    text = ""
    for page in doc:
        text += page.get_text()
    if DEBUG: print (text)
    return text

# utility function to read images from a PDF document
def read_images(file_path):
    doc = pymupdf.open(file_path)
    count = 0
    for page in doc:
        count += len(page.get_images(full=True))
    if DEBUG: print (count)
    return count