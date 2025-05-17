import re
from utils.pdf_parser import read_docs, detect_images
import os
from dotenv import load_dotenv

load_dotenv()
DEBUG = os.getenv("DEBUG", "false").lower() == "true"

SECTIONS = ["Experience", "Education", "Skills", "About Me", "Projects", "Contact"]

def detect_sections(text):
    found = []
    for section in SECTIONS:
        if re.search(rf'\b{section}\b', text, re.IGNORECASE):
            found.append(section)
    if DEBUG: print (found)
    return found

def check_cv(file_path):
    print(f"\n📄 Analyzing CV: {file_path}")
    text = read_docs(file_path)

    # Section Check
    print("\n📘 Section Check:")
    sections_found = detect_sections(text)
    for section in SECTIONS:
        print(f" - {section}: {'✅' if section in sections_found else '❌'}")

    # Image Check
    print("\n🖼️ Image Check:")
    img_count = detect_images(file_path)
    print(f" - Images found: {img_count} {'❌' if img_count > 0 else '✅'}")

    # Table/Column Heuristic (simple line count logic)
    line_lengths = [len(line) for line in text.split("\n") if line.strip()]
    long_lines = [l for l in line_lengths if l > 100]
    print("\n📏 Formatting Heuristic:")
    print(f" - Very long lines (>100 chars): {len(long_lines)} {'⚠️ Possibly multi-column' if len(long_lines) > 5 else '✅'}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python checker.py <your_cv.pdf>")
    else:
        check_cv(sys.argv[1])