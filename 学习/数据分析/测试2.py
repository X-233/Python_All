from sklearn.preprocessing import StandardScaler
import numpy as np

# 构造样本数据
X_train = np.array([[1, 2], [3, 4], [5, 6]])
X_test = np.array([[2, 3], [4, 5]])

# 创建StandardScaler对象
scaler = StandardScaler()

# 对训练集进行标准化
scaler.fit(X_train)
X_train_scaled = scaler.transform(X_train)

# 对测试集进行标准化
X_test_scaled = scaler.transform(X_test)
x = scaler.inverse_transform(X_test_scaled)
print("原始数据:\n", X_test)
print("标准化后的数据:\n", X_test_scaled)
print("还原的数据:\n", x)

