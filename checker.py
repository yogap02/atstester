# This script checks the formatting of a CV (Curriculum Vitae) PDF file.
# It looks for common sections, images, and formatting issues.  

import re
from utils.pdf_parser import read_docs, read_images
import os
from dotenv import load_dotenv

# fetch environment variables from .env to set DEBUG
load_dotenv()
DEBUG = os.getenv("DEBUG", "false").lower() == "true"

# Setting the sections to check for in the CV
# These are common sections found in CVs
SECTIONS = ["Experience", "Education", "Skills", "About Me", "Projects", "Contact"]

# This function checks for the presence of common CV sections
def detect_sections(text):
    found = []
    for section in SECTIONS:
        if re.search(rf'\b{section}\b', text, re.IGNORECASE):
            found.append(section)
    if DEBUG: print (found)
    return found

# This main function reads the CV file and checks for sections, images, and formatting
# It uses the read_docs and read_images functions from the pdf_parser module
def check_cv(file_path):
    print(f"\nAnalyzing CV: {file_path}")
    text = read_docs(file_path)

    # Section Check
    print("\nSection Check:")
    sections_found = detect_sections(text)
    for section in SECTIONS:
        print(f" - {section}: {'✅' if section in sections_found else '❌'}")

    # Image Check
    print("\nImage Check:")
    img_count = read_images(file_path)
    print(f" - Images found: {img_count} {'❌' if img_count > 0 else '✅'}")

    # Table/Column Heuristic (simple line count logic)
    line_lengths = [len(line) for line in text.split("\n") if line.strip()]
    long_lines = [l for l in line_lengths if l > 100]
    print("\nFormatting Heuristic:")
    print(f" - Very long lines (>100 chars): {len(long_lines)} {'Possibly multi-column' if len(long_lines) > 5 else '✅'}")

# This is the entry point of the script
if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python checker.py <your_cv.pdf>")
    else:
        check_cv(sys.argv[1])