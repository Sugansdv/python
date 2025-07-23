from fpdf import FPDF

def txt_to_pdf(txt_file, pdf_file):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    with open(txt_file, "r") as f:
        for line in f:
            pdf.cell(200, 10, txt=line.strip(), ln=True)

    pdf.output(pdf_file)
    print(f"Converted {txt_file} → {pdf_file}")

# Example
txt_to_pdf("notes.txt", "output.pdf")
