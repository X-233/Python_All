import torch
import numpy as np
from sklearn.preprocessing import MinMaxScaler

with open('data_1.text', 'r', encoding='utf-8') as f:
    data = eval(f.read())
x_1 = [[float(i['year'])] for i in data]
y_1 = [[float(sum(i['data_mon'].values())//len(data))] for i in data]

# 将数据进行归一化
scaler_x = MinMaxScaler()
scaler_y = MinMaxScaler()
data_x = scaler_x.fit_transform(x_1)
data_y = scaler_y.fit_transform(y_1)

def train_model(x_train, y_train, num_epochs=1000, lr=0.1):
    # 定义线性回归模型
    model = torch.nn.Linear(1, 1)  # 输入特征维度为1，输出特征维度为1

    # 定义损失函数和优化器
    criterion = torch.nn.MSELoss()  # 均方误差损失函数
    optimizer = torch.optim.SGD(model.parameters(), lr=lr)  # 随机梯度下降优化器，学习率为lr

    # 训练模型
    for epoch in range(num_epochs):
        # 前向传播计算模型输出
        y_pred = model(x_train)

        # 计算损失函数
        loss = criterion(y_pred, y_train)

        # 反向传播计算梯度和更新参数
        optimizer.zero_grad()  # 梯度清零
        loss.backward()  # 反向传播计算梯度
        optimizer.step()  # 更新参数

        # 打印训练信息
        if (epoch+1) % 100 == 0:
            print('Epoch [{}/{}], Loss: {:.4f}'.format(epoch+1, num_epochs, loss.item()))

    return model

def predict(model, x_test):
    # 使用模型进行预测
    y_pred = model(x_test)

    return y_pred.detach().numpy()

# 定义训练数据和测试数据
print(data_x)
print(data_y)
print()
x_train = torch.tensor(data_x, dtype=torch.float32)
y_train = torch.tensor(data_y, dtype=torch.float32)
x_test = scaler_x.fit_transform([[0], [2024.0], [2025.0], [2026.0], [2027.0]])
x_test = torch.tensor(x_test, dtype=torch.float32)

# 训练模型并进行预测
model = train_model(x_train, y_train)
y_pred = predict(model, x_test)

print('预测结果:', scaler_y.inverse_transform(y_pred))
