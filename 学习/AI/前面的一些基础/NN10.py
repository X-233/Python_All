import torch
import torch.nn as nn
import torchvision
from torch.nn import Conv2d, MaxPool2d, ReLU, Sigmoid
from torch.utils.data import DataLoader
from torch.utils.tensorboard import SummaryWriter

dataset = torchvision.datasets.CIFAR10('./test_s', train=True, transform=torchvision.transforms.ToTensor(), download=True)
dataloader = DataLoader(dataset=dataset, batch_size=64)

class Tudui(nn.Module):
    def __init__(self):
        super(Tudui, self).__init__()
        self.relu1 = ReLU()
        self.sigmoid = Sigmoid()

    def forward(self, x):
        x = self.sigmoid(x)
        return x

if __name__ == '__main__':
    input_1 = torch.tensor([[-1, 2], [2, -1]], dtype=torch.float32)
    input_1 = torch.reshape(input_1, (-1, 1, 2, 2))
    print(input_1.shape)
    print(input_1)

    tu = Tudui()
    output = tu(input_1)
    print(output)

    writer = SummaryWriter('relu1')
    step = 0
    for i in dataloader:
        img, tags = i
        writer.add_images('text', img, step)
        output = tu(img)
        writer.add_images('text1', output, step)
        step += 1
    writer.close()
