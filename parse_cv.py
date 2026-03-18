import pdfplumber

def extract_text_from_pdf(pdf_path, output_path):
    text = ""
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                text += page.extract_text() + "\n"
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(text)
        print("Done writing to " + output_path)
    except Exception as e:
        print(f"Error reading PDF: {e}")

if __name__ == "__main__":
    cv_path = "GIP2026-CV-BuiKhanhDuy.pdf"
    output_path = "cv_text.txt"
    extract_text_from_pdf(cv_path, output_path)
