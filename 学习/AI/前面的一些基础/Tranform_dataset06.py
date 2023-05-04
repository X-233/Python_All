from PIL import Image
from torch.utils.tensorboard import SummaryWriter
from torchvision import transforms
import torchvision

dataset_transform = transforms.Compose([
    torchvision.transforms.ToTensor()
])
train_s = torchvision.datasets.CIFAR10(root='./dataset', train=True, transform=dataset_transform, download=True)
text_s = torchvision.datasets.CIFAR10(root='./textset', train=False, transform=dataset_transform, download=True)

writer = SummaryWriter('p10')

for i in range(20):
    img, tag = train_s[i]
    writer.add_image('img', img, i)

writer.close()
