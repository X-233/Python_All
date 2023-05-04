import torch
import torch.nn as nn
import torchvision
from torch.nn import Conv2d, MaxPool2d, ReLU, Sigmoid, Linear, Flatten, Sequential
from torch.utils.data import DataLoader
from torch.utils.tensorboard import SummaryWriter

dataset = torchvision.datasets.CIFAR10('./test_s', train=True, transform=torchvision.transforms.ToTensor(), download=True)
dataloader = DataLoader(dataset=dataset, batch_size=64)

class Tudui(nn.Module):
    def __init__(self):
        super(Tudui, self).__init__()
        # self.conv2 = Conv2d(3, 32, 5, padding=2)
        # self.maxpool = MaxPool2d(2)
        # self.conv2_1 = Conv2d(32, 32, 5, padding=2)
        # self.maxpool_2 = MaxPool2d(2)
        # self.conv2_2 = Conv2d(32, 64, 5, padding=2)
        # self.maxpool_3 = MaxPool2d(2)
        # # 64*4*4=1024
        # self.flatten = Flatten()
        # self.linear1 = Linear(1024, out_features=64)
        # self.linear2 = Linear(64, out_features=10)

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
        # x = self.conv2(x)
        # x = self.maxpool(x)
        # x = self.conv2_1(x)
        # x = self.maxpool_2(x)
        # x = self.conv2_2(x)
        # x = self.maxpool_3(x)
        # x = self.flatten(x)
        # x = self.linear1(x)
        # x = self.linear2(x)
        x = self.model(x)
        return x

if __name__ == '__main__':
    tu = Tudui()
    # 验证
    input_1 = torch.ones((64, 3, 32, 32))
    output_1 = tu(input_1)
    print(output_1.shape)

    writer = SummaryWriter('seq')
    writer.add_graph(tu, input_1)
    writer.close()
