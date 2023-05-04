import torch
from torch import nn
from torch.utils.data import DataLoader
import torchvision
from torch.utils.tensorboard import SummaryWriter

train = torchvision.datasets.CIFAR10('./train_s', train=True, download=True, transform=torchvision.transforms.ToTensor())
test = torchvision.datasets.CIFAR10('./test_s', train=False, download=True, transform=torchvision.transforms.ToTensor())

# 1. 数据集长度
train_len = len(train)
test_len = len(test)
print('训练数据集长度:\t', train_len)
print('训练数据集长度:\t', test_len)
# 2. 利用Dataloader加载数据集
Dataloader_1 = DataLoader(dataset=train, batch_size=64, shuffle=True)
Dataloader_2 = DataLoader(dataset=test, batch_size=64, shuffle=True)

class Model1(nn.Module):
    def __init__(self):
        super(Model1, self).__init__()
        self.model = nn.Sequential(
            nn.Conv2d(3, 32, 5, padding=2),
            nn.MaxPool2d(2),
            nn.Conv2d(32, 32, 5, padding=2),
            nn.MaxPool2d(2),
            nn.Conv2d(32, 64, 5, padding=2),
            nn.MaxPool2d(2),
            # 扁平化
            nn.Flatten(),
            nn.Linear(1024, 64),
            # 分为十类
            nn.Linear(64, 10),
        )

    def forward(self, x):
        x = self.model(x)
        return x

    def load_model(self, name):
        self.model = torch.load(name)

# if __name__ == '__main__':
#     mel = Model1()
#     # 64张, 3通道, 32x32像素的图片
#     data = torch.ones((64, 3, 32, 32))
#     data_1 = mel(data)
#     print(data_1.shape)
