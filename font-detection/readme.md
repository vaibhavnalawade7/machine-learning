# README

This code uses `pytesseract` and `fontbakery` to identify the font used in an image.

## Dependencies

This code requires the following libraries:
- `pytesseract`
- `fontbakery`
- `cv2`

It also requires the `tesseract-ocr` library to be installed on your system. You can find installation instructions for `tesseract-ocr` here: https://github.com/UB-Mannheim/tesseract/wiki

## How to use

1. Replace the value of `image` with the path to the image you want to analyze.
2. Run the code.
3. The output will be the name of the font used in the image.

## Notes

- The code includes commented-out lines for cropping and resizing the image. You can uncomment and modify these lines to preprocess the image as needed.
- The image must be in a format that `cv2` can read (e.g. JPG, PNG).
- The code converts the image to grayscale before processing it. This can help improve the accuracy of the text recognition.

