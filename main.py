import matplotlib.pyplot as plt
from convert import datasets, my_img
from sklearn.cluster import KMeans, DBSCAN
from sklearn.svm import SVC
from sklearn.decomposition import PCA
from sklearn.ensemble import RandomForestClassifier

#主成分分析
pca = PCA(n_components=100, random_state=0)
X_pca = pca.fit_transform(datasets)

#k-means法クラスタリング
km = KMeans(n_clusters=10, random_state=0)
labels_km = km.fit_predict(X_pca)

#教師あり学習(分類)
model = RandomForestClassifier()
model.fit(datasets, labels_km)
print(model.predict(my_img))