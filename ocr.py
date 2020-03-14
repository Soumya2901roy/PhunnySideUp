import pytesseract as tess
import glob
import os
#tess.pytesseract.tesseract_cmd=r"C:\Users\Soumya\AppData\Local\Tesseract-OCR\tesseract.exe"
from PIL import Image

os.chdir(r'C:\Users\Soumya\Desktop\sarcastictales')
myjpgFiles=glob.glob('*.jpg')
with open('content.txt', 'a', encoding='utf-8') as file:
    for i in myjpgFiles:
        img=Image.open(i)
        text=tess.image_to_string(img)
        file.write(str(i))
        file.write('************************************************************\n')
        file.write(text)
        file.write('************************************************************\n')
        print(str(i))
file.close()
