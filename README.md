![CI](https://github.com/YOUR_USERNAME/YOUR_REPO_NAME/actions/workflows/ci.yml/badge.svg)


# 📄 PDF Page Insertion Script

This Python script merges multiple PDF files and inserts additional PDFs into specific positions of a base PDF.

It is especially useful for:

1. PDF formatting

2. Inserting approval pages

3. Adding pages

4. Creating a final compiled document

---

## 🚀 What This Script Does

The script:

1. Takes a base PDF
2. Inserts a second PDF after page 1
3. Inserts a third PDF after that
4. Appends the remaining pages of the base PDF
5. Saves the final combined document

---

## 📂 File Structure

Place the following files in the same directory:
```text

project-folder/
│
├── pdf.py
├── main_file.pdf
├── page_needed_to_added.pdf
├── next_page_needed_to_be_added.pdf
└── README.md
```

---

## 🛠 Requirements

Install the required package:

```sh
python -r requirements.txt
```

---

## ▶️ How to Run
```sh
python pdf.py
```

After execution, a new file will be created:
```text
Final.pdf
```

---

## 🧠 How It Works

The script uses pypdf:

- PdfReader → Reads existing PDF files
- PdfWriter → Writes and combines pages into a new PDF

Processing Order
- First page of main_file.pdf
- All pages from page_needed_to_added.pdf
- All pages from next_page_needed_to_be_added.pdf
- remaining pages from main_file.pdf

---

## 📌 Script Overview
```text
from pypdf import PdfReader, PdfWriter
```

1. Loads three PDFs
2. Creates a writer object
3. Adds pages in the required order
4. Writes output to a new file

---

## ⚙️ Customization

You can modify:

pdf1_path = "main_file.pdf"

pdf2_path = "page_needed_to_added.pdf"

pdf3_path = "next_page_needed_to_be_added.pdf"

output_path = "Master_Thesis_Akshay_Final.pdf"


To:

Change file names

Change insertion order

Add more PDFs

Insert at different page positions

---


## 🧩 Possible Improvements

1. Add command-line arguments
2. Add error handling
3. Allow dynamic page insertion positions
4. Convert into a reusable function
5. Add a GUI

---

## 🛑 Notes

1. All input files must exist in the same directory.
2. The script assumes main_file.pdf has at least one page.
3. File paths can be changed to absolute paths if needed.

---

## 📝 License

Free to use and modify.

---

_Thank You_
