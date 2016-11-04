import Image
import pytesseract
pic = Image.open('IMG_1385.JPG')
print pic.size, pic.im
pic.load()
pic.split()
print pic.split()
print(pytesseract.image_to_string(pic))
