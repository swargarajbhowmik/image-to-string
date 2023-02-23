# Importing Dependencies

import pytesseract
from PIL import Image

# Loading The Image

img = Image.open('img.png')

# Enhancing The Image

img = img.convert('L')

# Extracting The Text From Image
text = pytesseract.image_to_string(img)

# Printing The Text & Image

img.show()
print(text)