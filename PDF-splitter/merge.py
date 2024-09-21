import PyPDF2

def merge_pdfs(pdf1_path, pdf2_path, output_path):
    # Create a PDF merger object
    pdf_merger = PyPDF2.PdfMerger()

    # Open the first PDF and add it to the merger
    with open(pdf1_path, 'rb') as pdf1_file:
        pdf_merger.append(pdf1_file)

    # Open the second PDF and add it to the merger
    with open(pdf2_path, 'rb') as pdf2_file:
        pdf_merger.append(pdf2_file)

    # Write the merged PDF to the output file
    with open(output_path, 'wb') as output_pdf_file:
        pdf_merger.write(output_pdf_file)

    print(f"Merged PDF saved as {output_path}")

# Example usage:
pdf1 = 'chapter-15.1.pdf'
pdf2 = 'chapter-15.2.pdf'
output = 'chapter-15.pdf'

merge_pdfs(pdf1, pdf2, output)
