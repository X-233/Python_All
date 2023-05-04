import torch
import torch.nn as nn
import torch.nn.functional as F

class M(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        output = x + 1
        return output

if __name__ == '__main__':
    m = M()
    y = torch.tensor(1.0)
    x1 = m.forward(y)
    print(x1)
    input_1 = torch.tensor([[1, 2, 3, 4, 5],
                            [1, 2, 3, 4, 5],
                            [1, 2, 3, 4, 5],
                            [1, 2, 3, 4, 5],
                            [1, 2, 3, 4, 5]])

    kar = torch.tensor([[1, 1, 1],
                        [1, 0, 1],
                        [1, 1, 1]])

    input_1 = torch.reshape(input_1, (1, 1, 5, 5))
    kar = torch.reshape(kar, (1, 1, 3, 3))
    f1 = F.conv2d(input_1, kar, stride=1)
    print(f1)
