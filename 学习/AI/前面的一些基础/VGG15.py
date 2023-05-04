import torch
import torchvision

# train_data = torchvision.datasets.ImageNet('./ImageNet', split='train', download=True, transform=torchvision.transforms.ToTensor())
from torch import nn

vgg_true = torchvision.models.vgg16(progress=True)
vgg_false = torchvision.models.vgg16(progress=False)

# 保存方式1
# torch.save(vgg_false, 'vgg16_false.pth')

# 加载模型
# model = torch.load('vgg16_false.pth')

# 保存方式2
torch.save(vgg_true.state_dict(), 'vgg16_true.pth')

model = torch.load('vgg16_true.pth')
# 恢复成模型
vgg16 = torchvision.models.vgg16(progress=False)
vgg16.load_state_dict(torch.load('vgg16_true.pth'))
print(vgg16)

# 陷阱

