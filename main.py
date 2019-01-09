import networkx as nx
import community
import matplotlib.pyplot as plt
from convert import datasets
import matplotlib
from sklearn.cluster import KMeans

model = KMeans(n_clusters=100)
model.fit(datasets)

labels = model.labels_

print(labels)