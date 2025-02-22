import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from numpy import nonzero, array
from sklearn.cluster import KMeans
from sklearn.metrics import f1_score, accuracy_score, normalized_mutual_info_score, rand_score, adjusted_rand_score
from sklearn.preprocessing import LabelEncoder
from sklearn.decomposition import PCA

# 读取数据集
iris = pd.read_csv("dataset/Iris.csv", header=0)  # 鸢尾花数据集 Iris  class=3
wine = pd.read_csv("dataset/wine.csv")  # 葡萄酒数据集 Wine  class=3
seeds = pd.read_csv("dataset/seeds.csv")  # 小麦种子数据集 seeds  class=3
wdbc = pd.read_csv("dataset/wdbc.csv")  # 威斯康星州乳腺癌数据集 Breast Cancer Wisconsin (Diagnostic)  class=2
glass = pd.read_csv("dataset/glass.csv")  # 玻璃辨识数据集 Glass Identification  class=6
aggregation = pd.read_csv("dataset/aggregation.csv")  # class=7
flame = pd.read_csv("dataset/flame.csv")  # class=2
jain = pd.read_csv("dataset/jain.csv")  # class=2
spiral = pd.read_csv("dataset/spiral.csv")  # class=3
df = wine
print(df)

# 初始化数据集的参数
columns = list(df.columns) # 第一行为特征名
features = columns[:len(columns)-1] # 数据集的特征（除去最后一列的标签）
dataset = df[features] # 处理后的数据集
attributes = len(df.columns)-1 # 属性数量（数据集维度）
original_labels = list(df[columns[-1]]) # 原始标签

def initialize_centroids(data, k):
    # 随机选择第一个质心
    centers = [data[np.random.randint(data.shape[0])]]
    
    for _ in range(1, k):
        # 计算每个点到已有质心的距离的平方
        distances = np.linalg.norm(data[:, np.newaxis] - centers[-1], axis=2)
        distances = np.minimum(distances, np.inf)
        
        # 对于每个点，选择其与最近质心的距离的平方作为权重
        weights = distances ** 2
        weights /= weights.sum()
        
        # 从数据集中随机选择下一个质心
        r = np.random.rand()
        cumulative_sum = np.cumsum(weights)
        center_index = np.where(cumulative_sum >= r)[0][0]
        centers.append(data[center_index])
    
    return np.array(centers)

def get_clusters(data,centroids):
    # 计算数据点与质心之间的距离，并将数据点分配给最近的质心
    distances = np.linalg.norm(data[:, np.newaxis] - centroids, axis=2)
    cluster_labels = np.argmin(distances, axis=1)
    return cluster_labels

def update_centroids(data,cluster_labels,k):
    # 计算每个簇的新质心，即簇内数据点的均值
    new_centroids = np.array([data[cluster_labels == i].mean(axis=0) for i in range(k)])
    return new_centroids

def k_means(data, k, T, epsilon):
    # 初始化质心
    centroids = initialize_centroids(data,k)
    t = 0
    while t <= T:
        # 分配簇
        cluster_labels = get_clusters(data,centroids)

        # 更新质心
        new_centroids = update_centroids(data,cluster_labels,k)

        # 检查收敛条件
        if np.linalg.norm(new_centroids - centroids) < epsilon:
            break
        centroids = new_centroids
        print("第", t, "次迭代")
        t += 1
    return cluster_labels, centroids


# 计算聚类指标
def clustering_indicators(labels_true, labels_pred):
    if type(labels_true[0]) != int:
        labels_true = LabelEncoder().fit_transform(df[columns[len(columns) - 1]])  # 如果数据集的标签为文本类型，把文本标签转换为数字标签
    f_measure = f1_score(labels_true, labels_pred, average='macro')  # F值
    accuracy = accuracy_score(labels_true, labels_pred)  # ACC
    normalized_mutual_information = normalized_mutual_info_score(labels_true, labels_pred)  # NMI
    rand_index = rand_score(labels_true, labels_pred)  # RI
    ARI = adjusted_rand_score(labels_true, labels_pred) #ARI
    return f_measure, accuracy, normalized_mutual_information, rand_index, ARI

# 绘制聚类结果散点图
def draw_cluster(dataset, centers, labels):
    center_array = array(centers)
    if attributes > 2:
        dataset = PCA(n_components=2).fit_transform(dataset)  # 如果属性数量大于2，降维
        center_array = PCA(n_components=2).fit_transform(center_array)  # 如果属性数量大于2，降维
    else:
        dataset = array(dataset)
    
    # 做散点图
    label = array(labels)
    plt.scatter(dataset[:, 0], dataset[:, 1], marker='o', c='black', s=7)  # 原图

    colors = np.array(
        ["#FF0000", "#0000FF", "#00FF00", "#FFFF00", "#00FFFF", "#FF00FF", "#800000", "#008000", "#000080", "#808000",
         "#800080", "#008080", "#444444", "#FFD700", "#008080"])
    
    # 循换打印k个簇，每个簇使用不同的颜色
    for i in range(k):
        plt.scatter(dataset[nonzero(label == i), 0], dataset[nonzero(label == i), 1], c=colors[i], s=7, marker='o')
        plt.scatter(center_array[:, 0], center_array[:, 1], marker='x', color='m', s=30)
    
    # 设置x和y坐标轴刻度的标签字体和字号
    plt.xticks(fontproperties='Times New Roman', fontsize=10.5)
    plt.yticks(fontproperties='Times New Roman', fontsize=10.5)
    plt.xlabel("x - label", fontdict={'family': 'Times New Roman', 'size': 10.5}, loc="right")
    plt.ylabel("y - label", fontdict={'family': 'Times New Roman', 'size': 10.5}, loc="top")

    plt.show()

if __name__ == "__main__":
    k = 3 # 聚类簇数
    T = 100 # 最大迭代次数
    n = len(dataset) # 样本数量
    epsilon = 1e-5
    # 聚类结果
    labels, centers = k_means(np.array(dataset), k, T, epsilon)
    print(labels)
    # 聚类指标
    F_measure, ACC, NMI, RI, ARI = clustering_indicators(original_labels, labels)
    print("F_measure:", F_measure, "ACC:", ACC, "NMI", NMI, "RI", RI, "ARI", ARI)
    # 可视化
    draw_cluster(dataset, centers, labels=labels)
