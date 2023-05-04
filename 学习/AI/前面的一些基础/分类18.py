import torch
from torch import nn
from torch.utils.data import DataLoader
import torchvision
from torch.utils.tensorboard import SummaryWriter

train = torchvision.datasets.CIFAR10('./train_s', train=True, download=True, transform=torchvision.transforms.ToTensor())
test = torchvision.datasets.CIFAR10('./test_s', train=False, download=True, transform=torchvision.transforms.ToTensor())

# 1. 数据集长度
train_len = len(train)
test_len = len(test)
print('训练数据集长度:\t', train_len)
print('训练数据集长度:\t', test_len)
# 2. 利用Dataloader加载数据集
Dataloader_1 = DataLoader(dataset=train, batch_size=64, shuffle=True)
Dataloader_2 = DataLoader(dataset=test, batch_size=64, shuffle=True)

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

    def load_model(self, name):
        self.model = torch.load(name)

if __name__ == '__main__':
    # 1.传入模型
    mod1 = Model1()
    # 1.2 改成GPU
    device = torch.device('cpu')
    mod1 = mod1.to(device)
    # mod1 = mod1.cuda()

    # 2.定义损失函数
    loss = nn.CrossEntropyLoss()
    loss = loss.to(device)

    # 3.优化器, mod1.parameters()
    lr_rate = 0.02
    optim = torch.optim.SGD(params=mod1.parameters(), lr=lr_rate)

    # 4.设置网络参数
    # 4.1 记录训练次数
    train_step = 0
    # 4.2 记录测试次数
    test_step = 0
    # 4.3 训练轮数
    epoch = 20
    # 4.4 画图
    writer = SummaryWriter('trains')

    # 5. 训练开始
    for i in range(epoch):
        print('***************第 {} 轮训练*****************'.format(i + 1))
        for j in Dataloader_1:
            images, tags = j
            images = images.to(device)
            tags = tags.to(device)
            output = mod1(images)

            # 计算损失
            result = loss(output, tags)

            # 反向传播, 清除求导
            optim.zero_grad()
            result.backward()

            # 进行优化
            optim.step()

            # 测试
            train_step += 1
            if train_step % 100 == 0:
                print('第 {} 次训练, loss = {}'.format(train_step, result.item()))
                # print(output.argmax(1))
                # print(tags)
                writer.add_scalar('loss', result.item(), global_step=train_step)

        # 测试开始
        total_test_loss = 0
        total_accuracy = 0
        with torch.no_grad():
            for j in Dataloader_2:
                images, tags = j
                images = images.to(device)
                tags = tags.to(device)
                output = mod1(images)
                # 计算损失
                result = loss(output, tags)
                total_test_loss += result.item()
                test_step += 1

                # 对比, 横向
                accuracy = (output.argmax(1) == tags).sum()
                total_accuracy += accuracy

        # 测试loss
        print('total_test_loss = {}'.format(total_test_loss))
        # 准确率
        print('整体的一个正确率 {} '.format(total_accuracy / test_len))
        writer.add_scalar('test_loss', total_test_loss, global_step=test_step)

        # 保存模型
        torch.save(mod1, 'models{}.pth'.format(i))
    writer.close()
