from PIL import Image
from torch.utils.tensorboard import SummaryWriter
from torchvision import transforms

# 图片需要一个tensor的数据类型
img_path = "D:\图片\艾米莉亚\艾米莉亚_3.jpg"
img = Image.open(img_path)

writer = SummaryWriter('logs')
tensor = transforms.ToTensor()
trains_tensor = tensor(img)

writer.add_image('text1', trains_tensor)
print(trains_tensor[0][0][0])
trans_norm = transforms.Normalize([0.5, 0.5, 0.5], [0.5, 0.5, 0.5])
img_norm = trans_norm(trains_tensor)
print(img_norm[0][0][0])
writer.add_image('text2', img_norm, 1)

trans_size = transforms.Resize((512, 512))
img_size = trans_size(img)
trains_tensor = tensor(img_size)
print(trains_tensor[0][0][0])
writer.add_image('text3', trains_tensor, 2)

trains_resize_2 = transforms.Resize(512)
trains_com = transforms.Compose([trains_resize_2, tensor])
img_size_2 = trains_com(img)
writer.add_image('text4', img_size_2, 0)


writer.close()

