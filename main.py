import glob
from pathlib import Path
from fpdf import FPDF

filepaths = glob.glob("textFiles/*.txt")

for filepath in filepaths:
    filename = Path(filepath).stem
    print(filename)
    # with open(filepath,'w') as file:
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt= filename)

    with open(filepath,'r') as file:
        filedata = file.readline()
    
    pdf.ln(20)
    pdf.set_font(family="Times", size=12, style="B")
    pdf.multi_cell(w=0, h=8, txt=filedata )
    pdf.output(f"PDFs/{filename}.pdf")