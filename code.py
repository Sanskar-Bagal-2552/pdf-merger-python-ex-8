from pypdf import PdfWriter, PdfReader
import os

writer = PdfWriter()

# Get all PDF files
files = [file for file in os.listdir() if file.endswith(".pdf")]

for pdf in files:
    reader = PdfReader(pdf)
    for page in reader.pages:
        writer.add_page(page)

with open("merged_pdf.pdf", "wb") as f:
    writer.write(f)
