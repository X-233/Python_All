from torch.utils.tensorboard import SummaryWriter
import numpy as np
from PIL import Image

writer = SummaryWriter('logs')
img_path = "D:\图片\艾米莉亚\艾米莉亚_0.jpg"
img_PIL = Image.open(img_path)
img_array = np.array(img_PIL)
print(img_array.shape)
writer.add_image('text1', img_array, 2, dataformats='HWC')

for i in range(100):
    writer.add_scalar('y=x', i, i)

writer.close()
