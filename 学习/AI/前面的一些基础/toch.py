# 1、爬虫速度不要太快，不要给对方服务器造成太大压力
# 2、爬虫不要伪造VIP，绕过对方身份验证，可以买一个VIP做自动化
# 3、公民个人信息不要去碰
import torch


# def get_device():
#     return torch.device("cuda" if torch.cuda.is_available() else "cpu")
#
#
# cpus = get_device()
#
# print(cpus)

x = torch.arange(4.0)
x.requires_grad(True)
y = 2 * torch.dot(x, x)
print(x)
