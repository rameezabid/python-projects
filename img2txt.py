import pytesseract
from PIL import Image

# Open image using PIL
image = Image.open('convert.jpg')

# Convert image to text using pytesseract
text = pytesseract.image_to_string(image, lang = 'ara')

# Print the text
print(text)