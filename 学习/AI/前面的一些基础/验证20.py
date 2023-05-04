import os

import torch
import torchvision
from PIL import Image
import torch.nn as nn

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

if __name__ == '__main__':
    transform = torchvision.transforms.Compose([
        torchvision.transforms.Resize((32, 32)),
        torchvision.transforms.ToTensor()
    ])
    mod2 = torch.load('models100.pth', map_location=torch.device('cpu'))
    # 测试
    mod2.eval()

    img_path = os.listdir(r'D:\IDEA\Project\学习\学习\图片\images\飞机')
    right = 0
    right1 = 1
    for i in img_path:
        img = Image.open('D:\\IDEA\\Project\\学习\\学习\\图片\\images\\飞机\\' + i)
        img = img.convert('RGB')
        img = transform(img)
        img = torch.reshape(img, (1, 3, 32, 32))
        with torch.no_grad():
            output = mod2(img)
        if output.argmax(1) == 0:
            right += 1
        else:
            print('没有识别出\t', i)
        right1 += 1
    accuracy = right / right1
    print('正确率为\t', accuracy)
    r = {'airplane': 0, 'automobile': 1, 'bird': 2, 'cat': 3, 'deer': 4, 'dog': 5, 'frog': 6, 'horse': 7, 'ship': 8, 'truck': 9}
