from PIL import Image
from torch.utils.tensorboard import SummaryWriter
from torchvision import transforms

# 图片需要一个tensor的数据类型

img_path = "D:\图片\艾米莉亚\艾米莉亚_3.jpg"
img = Image.open(img_path)

writer = SummaryWriter('logs')

tensor_img = transforms.ToTensor()
tensor_trans = tensor_img(img)

print(tensor_trans)

writer.add_image('text3', tensor_trans)
writer.close()
