import torchvision

# train_data = torchvision.datasets.ImageNet('./ImageNet', split='train', download=True, transform=torchvision.transforms.ToTensor())
from torch import nn

vgg_true = torchvision.models.vgg16(progress=True)
vgg_false = torchvision.models.vgg16(progress=False)

vgg_true.classifier.add_module('(7)add_linear', nn.Linear(1000, 10))
print(vgg_true)

# 10个类别
vgg_false.classifier[6] = nn.Linear(4096, 10)
print(vgg_false)
