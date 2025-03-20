import cv2
import pytesseract

# 读取图片
img_url = './images/grsds.jpg'
image = cv2.imread(img_url)
# 使用pytesseract进行OCR识别
data = pytesseract.image_to_string(image, lang='eng', config='--psm 7')
print(data)