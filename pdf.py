from pypdf import PdfReader, PdfWriter

pdf1_path = "Master_Thesis_Akshay__Initial.pdf"  # base PDF
pdf2_path = "Declaration of Authorship.pdf"  # to insert at page 2
pdf3_path = "Examination Office - Declaration on AI-Usage.pdf"  # to insert at page 3
output_path = "Master_Thesis_Akshay_Final.pdf"

reader1 = PdfReader(pdf1_path)
reader2 = PdfReader(pdf2_path)
reader3 = PdfReader(pdf3_path)

writer = PdfWriter()

# --- Add first page of PDF 1 ---
writer.add_page(reader1.pages[0])

# --- Insert PDF 2 ---
for page in reader2.pages:
    writer.add_page(page)

# --- Insert PDF 3 ---
for page in reader3.pages:
    writer.add_page(page)

# --- Add remaining pages of PDF 1 ---
for page in reader1.pages[1:]:
    writer.add_page(page)

# --- Save result ---
with open(output_path, "wb") as f:
    writer.write(f)

print(f"New PDF created: {output_path}")
