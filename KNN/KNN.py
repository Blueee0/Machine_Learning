import numpy as np
import pandas as pd
import operator

# 读取数据集
iris = pd.read_csv("dataset/Iris.csv", header=0)  # 鸢尾花数据集 Iris  class=3
wine = pd.read_csv("dataset/wine.csv")  # 葡萄酒数据集 Wine  class=3
seeds = pd.read_csv("dataset/seeds.csv")  # 小麦种子数据集 seeds  class=3
wdbc = pd.read_csv("dataset/wdbc.csv")  # 威斯康星州乳腺癌数据集 Breast Cancer Wisconsin (Diagnostic)  class=2
glass = pd.read_csv("dataset/glass.csv")  # 玻璃辨识数据集 Glass Identification  class=6
df = iris # 设置要读取的数据集
print(df)

# 初始化数据集的参数
columns = list(df.columns)
features = columns[:-1]  # 特征名
dataset = df[features].values  # 数据集
class_labels = df[columns[-1]].values  # 原始标签
# 分为训练集和测试集
N = int(df.shape[0])
N_train = int(N * 0.7)
N_test = N-N_train

perm = np.random.permutation(N)
index_train = perm[:N_train]
index_test = perm[N_train:]

data_train = dataset[index_train, :]
lab_train = class_labels[index_train]
data_test = dataset[index_test, :]
lab_test = class_labels[index_test]

def KNN(trainData,testData,labels,k):
    # 计算该样本与所有训练样本之间的距离
    distances = np.sqrt(((trainData - testData) ** 2).sum(axis=1))
    # 获取最近的k个样本的索引
    nearest_indices = distances.argsort()[:k]
    # 统计类别
    class_counts = np.unique(labels[nearest_indices], return_counts=True)
    # 返回出现次数最多的类别
    return class_counts[0][np.argmax(class_counts[1])]


if __name__ == "__main__":
    k = 5
    right_num = 0

    for i in range(N_test):
        test = data_test[i,:]
        det = KNN(data_train,test,lab_train,k)
        if det == lab_test[i]:
            right_num +=1
        print('Sample %d  lab_ture = %s  lab_det = %s' % (i, lab_test[i], det))

    print('Accuracy = %.2f %%' % (right_num * 100 / N_test))

