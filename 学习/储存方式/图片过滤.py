import hashlib
from PIL import Image

if __name__ == '__main__':
    # 打开图像并将其转换为灰度图像
    # img = Image.open("1.jpg").convert('L')
    # 打开图像并将其缩放到32x32像素大小,转换为灰度图像
    img = Image.open("1.jpg").resize((32, 32)).convert('L')
    img1 = Image.open("2.jpg").resize((32, 32)).convert('L')

    # 将图像数据转换为一维数组
    data = list(img.getdata())
    data1 = list(img1.getdata())

    md_1 = hashlib.md5(str(data).encode('utf-8')).hexdigest()
    md_2 = hashlib.md5(str(data1).encode('utf-8')).hexdigest()

    print(md_1)
    print(md_2)
