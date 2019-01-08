import networkx as nx
import community
import matplotlib.pyplot as plt

G = nx.karate_club_graph()

# クラスタリング
partition = community.best_partition(G)

print(partition)