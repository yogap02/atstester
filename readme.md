## ATS Tester - checker.py - 2025

# A tool to help check whether our CV is already good enough for ATS machine or not.

## Standards within this tools

# Tools checking if this heading label or section label are presents in the documents : 
- Experience    : Ressemble part containing infromation related to work experiences
- Education     : Inspecting part if education history or any similar information with education label existed.
- Skill         : Looking for a section containing skill is present
- About Me      : Check if abount me section mentioned in the pdf file.
- Projects      : Ressemble of the projects history of portofolio stated in the CV
- Contact       : Inspect if the contact infromation shown in the pdf
- Image(s)      : Counting all available image
- Long Line(s)  : Detect if a line with more than 100 characters is present

## Disclaimer 
There is no guarantee that this checker suffice to comply with all ATS engine, the scope is aforementioned and only that.

## Getting Started
1. Go to root folder
2. Create venv `python -m venv venv`
3. Activate venv 
    - Windows `source venv/Scripts/activate`
    - Linux `source ./venv/bin/activate`
4. Once activated you will see (pymupdf-venv) shown in the terminal
5. Put <your.pdf> in the root folder
6. Execute checker.py `python checker.py <your.pdf>`