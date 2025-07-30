import PyPDF2

def extract_text(pdf_path):
    try:
        with open(pdf_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)

            if reader.is_encrypted:
                raise ValueError("PDF is encrypted and cannot be read.")

            for page_num, page in enumerate(reader.pages):
                text = page.extract_text()
                if text:
                    yield f"[Page {page_num+1}]\n" + text.strip()
                else:
                    yield f"[Page {page_num+1}]\n(No text found)"
    except FileNotFoundError:
        raise FileNotFoundError("PDF file not found.")
    except Exception as e:
        raise e
