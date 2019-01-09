import pandas as pd
import mahotas as mh
import numpy as np
from glob import glob
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans

#画像の取得
imgs = glob("./material_images/*.png") + glob("./material_images/*.jpg")
alldescriptors = []

#グレイスケール
for im in imgs:
    im = mh.imread(im, as_gray=True)
    im = im.astype(np.uint8)
    alldescriptors.append(surf.surf(im, descriptor_only=True))

# df = pd.read_csv("./pokemon.csv", header=None)
# X, y = df.iloc[1:, 1:].values, df.iloc[1:, 0].values
# sc = StandardScaler()
