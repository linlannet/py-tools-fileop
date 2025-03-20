from rapidocr import RapidOCR

engine = RapidOCR()
img_url = './images/grsds.jpg'
# img_url = "https://github.com/RapidAI/RapidOCR/blob/main/python/tests/test_files/ch_en_num.jpg?raw=true"
result = engine(img_url)
print(result)

result.vis()