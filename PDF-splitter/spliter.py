import PyPDF2

def split_pdf(input_pdf_path, output_prefix, ranges):
    # Open the input PDF
    with open(input_pdf_path, 'rb') as input_pdf_file:
        pdf_reader = PyPDF2.PdfReader(input_pdf_file)

        for idx, page_range in enumerate(ranges):
            # Create a PDF writer for each range
            pdf_writer = PyPDF2.PdfWriter()

            start_page, end_page = page_range
            for page_num in range(start_page - 1, end_page):
                pdf_writer.add_page(pdf_reader.pages[page_num])

            # Save the output PDF
            output_pdf_path = f"{output_prefix}-{idx + 1}.pdf"
            with open(output_pdf_path, 'wb') as output_pdf_file:
                pdf_writer.write(output_pdf_file)

            print(f"Created {output_pdf_path}")

# Example usage:
input_pdf = 'main-image-book/book-3.pdf'
output_prefix = 'chapter'
ranges = [(1,7),(8,11),(12,50),(52,75),(76,82),(84,89),(90,186)]  # Split by page ranges (inclusive)

split_pdf(input_pdf, output_prefix, ranges)
