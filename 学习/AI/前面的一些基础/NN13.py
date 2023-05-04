import torch
import torch.nn as nn
import torchvision
from torch.nn import Conv2d, MaxPool2d, ReLU, Sigmoid, Linear, Flatten, Sequential
from torch.utils.data import DataLoader
from torch.utils.tensorboard import SummaryWriter

dataset = torchvision.datasets.CIFAR10('./test_s', train=False, transform=torchvision.transforms.ToTensor(), download=True)
dataloader = DataLoader(dataset=dataset, batch_size=64)

class Tudui(nn.Module):
    def __init__(self):
        super(Tudui, self).__init__()
        self.model = Sequential(
            Conv2d(3, 32, 5, padding=2),
            MaxPool2d(2),
            Conv2d(32, 32, 5, padding=2),
            MaxPool2d(2),
            Conv2d(32, 64, 5, padding=2),
            MaxPool2d(2),
            Flatten(),
            Linear(1024, out_features=64),
            Linear(64, out_features=10)
        )

    def forward(self, x):
        x = self.model(x)
        return x

if __name__ == '__main__':
    tu = Tudui()
    # 验证
    # input_1 = torch.ones((64, 3, 32, 32))
    # output_1 = tu(input_1)
    optim = torch.optim.SGD(params=tu.parameters(), lr=0.1)
    loss = nn.CrossEntropyLoss()
    for epoc in range(20):
        running = 0.0
        for i in dataloader:
            images, tags = i
            output_1 = tu(images)
            print(tags)
            # 计算损失函数
            result_loss = loss(output_1, tags)
            # 求导清零
            optim.zero_grad()
            # 反向传播
            result_loss.backward()
            optim.step()

            running += result_loss
        print(running)
