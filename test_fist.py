import pdfplumber

with pdfplumber.open("example.pdf") as pdf:
    print(pdf.pages.__len__())  # or len(pdf.pages)
