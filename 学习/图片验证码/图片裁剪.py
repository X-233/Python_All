from PIL import Image

def caijian(imgs):
    # 打开图片
    img = Image.open(imgs[0])
    img_1 = Image.open(imgs[1])

    # 获取宽高
    width, height = img.size
    print(width, height)
    width_1, height_1 = img_1.size
    print(width_1, height_1)

    # 定义目标宽高
    target_width = width_1
    target_height = height_1

    # 调整图片大小并填充黑色
    new_img = Image.new('RGB', (target_width, target_height), color='black')
    img.thumbnail((target_width, target_height))
    new_img.paste(img, (int((target_width - img.size[0]) / 2), int((target_height - img.size[1]) / 2)))

    # 保存图片
    new_img.save(imgs[0])

caijian(['_tu2.png', '_tu1.png'])