import pytesseract
from PIL import Image
import cv2
import numpy as np

def preprocess_image(image: Image.Image):
    image = np.array(image)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY)
    return thresh

def extract_text_from_image(image: Image.Image) -> str:
    processed = preprocess_image(image)
    return pytesseract.image_to_string(Image.fromarray(processed))
