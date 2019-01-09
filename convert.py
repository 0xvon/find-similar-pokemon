import numpy as np
from PIL import Image
from glob import glob

#画像の取得
imgs = glob("./material_images/*.png") + glob("./material_images/*.jpg")

#画像の処理・配列化
datasets = []
for i in imgs:
    img = Image.open(i)
    img = img.convert('L')
    img = img.resize((100, 100))
    img = np.array(img)
    img = img.ravel()
    datasets.append(img)

#自身の画像の読み込み
my_img = Image.open("./my_image")
my_img = my_img.convert("L")
my_img = my_img.resize((100, 100))
my_img = np.array(my_img)
my_img = my_img.revel()