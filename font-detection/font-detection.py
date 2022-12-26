import pytesseract
import fontbakery
import cv2

# Read the image
image = cv2.imread('image.jpg')

# Preprocess the image (e.g. crop, resize, convert to grayscale)
# Crop the image to focus on the text
#cropped_image = image[100:200, 200:300]

# Resize the image to a standard size (e.g. 300x300)
#resized_image = cv2.resize(cropped_image, (300, 300))

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Extract the text from the image using pytesseract
text = pytesseract.image_to_string(gray_image)

# Identify the font using fonttools
font = fontbakery.identify_font(text)

# Output the result
print(f'The font used in the image is: {font}')
