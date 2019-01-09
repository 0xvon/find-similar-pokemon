import pandas as pd
import mahotas as mh
import numpy as np
from PIL import Image
import cv2
from glob import glob
from skimage import data
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans

#画像の取得
imgs = glob("./material_images/*.png") + glob("./material_images/*.jpg")

#画像の処理
datasets = []
for i in imgs:
    img = Image.open(i)
    img = img.convert('L')
    img = img.resize((100, 100))
    img = np.array(img)
    img = img.flatten()
    datasets.append(img)

    # datasets.append(img)

print(datasets)