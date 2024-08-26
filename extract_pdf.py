"""
below dependencies are required

pip install pymupdf
pip install fitz
pip install frontend

"""

import pymupdf

file_path = "C:\\Users\\mohan\\Downloads\\file23.pdf"

def get_page_obj():
    doc = pymupdf.open(file_path)
    return doc.load_page(0)

def print_text(page):
    print(page.get_text("text"))


def main():
  print_text(get_page_obj())

if __name__ == '__main__':
    main()