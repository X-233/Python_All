import torch
import torch.nn as nn
import torchvision
from torch.nn import Conv2d, MaxPool2d
from torch.utils.data import DataLoader
from torch.utils.tensorboard import SummaryWriter

dataset = torchvision.datasets.CIFAR10('./test_s', train=True, transform=torchvision.transforms.ToTensor(), download=True)
dataloader = DataLoader(dataset=dataset, batch_size=64)

class Tudui(nn.Module):
    def __init__(self):
        super(Tudui, self).__init__()
        # stride默认size是卷积核的size
        self.maxpool1 = MaxPool2d(kernel_size=3, ceil_mode=True)

    def forward(self, x):
        x = self.maxpool1(x)
        return x

if __name__ == '__main__':
    input_1 = torch.tensor([[1, 2, 0, 3, 1],
                            [1, 2, 0, 0, 0],
                            [1, 2, 0, 0, 0],
                            [1, 2, 0, 0, 0],
                            [1, 2, 0, 0, 0]], dtype=torch.float32)
    input_1 = torch.reshape(input_1, (-1, 1, 5, 5))
    tu = Tudui()
    output = tu(input_1)
    print(output)

    writer = SummaryWriter('maxpool')
    step = 0
    for i in dataloader:
        img, tags = i
        writer.add_images('text', img, step)
        output = tu(img)
        writer.add_images('text1', output, step)
        step += 1
    writer.close()
