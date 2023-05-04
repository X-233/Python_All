import torch
import torch.nn as nn
import torch.nn.functional as F
import torchvision
from torch.nn import Conv2d
from torch.utils.data import DataLoader


dataset = torchvision.datasets.CIFAR10('./train_s', train=True, transform=torchvision.transforms.ToTensor(), download=True)
dataloader = DataLoader(dataset=dataset, batch_size=64)

class Tudui(nn.Module):
    def __init__(self):
        super(Tudui, self).__init__()
        self.conv1 = Conv2d(in_channels=3, out_channels=6, kernel_size=3, stride=1, padding=0)

    def forward(self, x):
        x = self.conv1(x)
        return x

if __name__ == '__main__':
    tu = Tudui()
    for i in dataloader:
        imgs, tags = i
        output = tu(imgs)
        print(output.shape)
