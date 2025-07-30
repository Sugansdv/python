from extractor.reader import extract_text

if __name__ == "__main__":
    pdf_path = "sample.pdf"
    try:
        for page_text in extract_text(pdf_path):
            print("------ PAGE ------")
            print(page_text.strip())
    except Exception as e:
        print(f" Error: {e}")
