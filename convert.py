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
