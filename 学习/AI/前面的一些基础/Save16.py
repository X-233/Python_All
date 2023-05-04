import torch
import torch.nn as nn
import torchvision
from torch.nn import Conv2d, MaxPool2d, ReLU, Sigmoid, Linear, Flatten, Sequential
from torch.utils.data import DataLoader
from torch.utils.tensorboard import SummaryWriter

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
    # tu = Tudui()
    # torch.save(tu, 'tudui.pth')

    tu = torch.load('tudui.pth')
    print(tu)
