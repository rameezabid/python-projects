import PyPDF2

# Open the PDF file in read binary mode
pdf_file = open('convert.pdf', 'rb')

# Create a PDF reader object
pdf_reader = PyPDF2.PdfReader(pdf_file)

# Get the total number of pages in the PDF file
num_pages = len(pdf_reader.pages)

# Create an empty string to store the extracted text
text = ""

# Loop through each page and extract the text
for page in range(num_pages):
    page_obj = pdf_reader.pages[page]
    extracted_text = page_obj.extract_text()
    text += extracted_text

# Close the PDF file
pdf_file.close()

# Print the extracted text
print(text)