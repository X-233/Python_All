# 1、爬虫速度不要太快，不要给对方服务器造成太大压力
# 2、爬虫不要伪造VIP，绕过对方身份验证，可以买一个VIP做自动化
# 3、公民个人信息不要去碰
from torch.utils.data import Dataset
import cv2
from PIL import Image
import os

class Mydata(Dataset):

    def __init__(self, root_dir, data_dir):
        self.root_dir = root_dir
        self.data_dir = data_dir
        self.dir = os.path.join(self.root_dir, self.data_dir)
        self.img_list = os.listdir(self.dir)

    def __getitem__(self, key):
        # img_path = 'D:\图片\艾米莉亚\艾米莉亚_0.jpg'
        # Image.open(img_path)
        img_name = self.img_list[key]
        img_name_path = os.path.join(self.root_dir, self.data_dir, img_name)
        img = Image.open(img_name_path)
        label = self.data_dir
        return img, label

    def __len__(self):
        return len(self.img_list)

if __name__ == '__main__':
    data = Mydata('D:\图片', '康娜')
    img_1, label_1 = data[0]
    img_1.show()
