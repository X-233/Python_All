import parsel
import requests
import torch
from sklearn.preprocessing import MinMaxScaler, StandardScaler
import pickle

class Get_data:
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    }

    params = {
        'nian': '',
        'catid': '4',
        'host': 'fangjia',
    }

    url = 'https://www.gotohui.com/index.php?index/rzoushi'
    data = []

    @staticmethod
    def get(func):
        """
        :param func: requests.post方法
        :return: 返回
        """
        def wrapper(*args):
            html_1 = func(*args)
            select = parsel.Selector(html_1.text)

            # 数据提取
            data_1 = select.xpath('//script')
            data_2 = data_1.re('labels: \[(.*?)\]')[0]
            data_3 = data_1.re('data: \[([\s\S]*?)\],')[0]

            # 数据处理
            x = [j.replace('\'', '') for j in data_2.split(',')]
            data_3 = data_3.replace('\n', '').replace(' ', '')
            if data_3[-1] == ',':
                data_3 = data_3.rsplit(',', 1)[0]
            y_1 = data_3.split(',')
            y = [int(j) for j in y_1]
            y_2 = sum(y) / len(y) / 2
            for j in y:
                if j < y_2:
                    y[y.index(j)] = int(y_2*2 + y_2*0.2)

            # 数据融合
            x_y = dict(zip(x, y))
            print(x, y)
            return x_y
        return wrapper

    @staticmethod
    @get
    def post_html(years):
        Get_data.params['nian'] = years
        html1 = requests.post(url=Get_data.url, headers=Get_data.headers, data=Get_data.params)
        return html1

    @staticmethod
    def start():
        for i in range(2011, 2023):
            Get_data.data.append({'year': i, 'data_mon': Get_data.post_html(i)})
        # 存储数据
        with open('data_1.text', 'w', encoding='utf-8') as f:
            f.write(str(Get_data.data))

class Predict:
    with open('data_1.text', 'r', encoding='utf-8')as f:
        data = eval(f.read())

    def __init__(self):
        self.x = None
        self.y = None

        # 定义模型
        self.bias = torch.zeros(1, requires_grad=True)
        self.weight = torch.randn((1, 1), requires_grad=True)

        # 定义损失函数和优化器
        self.criterion = torch.nn.MSELoss()
        self.optimizer = torch.optim.SGD([self.weight, self.bias], lr=0.1)

        # 归一化
        # self.scaler_x = MinMaxScaler()
        self.scaler_x = StandardScaler()
        # self.scaler_y = MinMaxScaler()
        self.scaler_y = StandardScaler()

        self.model = None

    # 定义模型
    def linear_regression(self, x_data):
        self.model = torch.matmul(x_data, self.weight) + self.bias
        return self.model

    def get_standard_data(self):
        x = [[i['year']] for i in Predict.data]
        y = [[sum(i['data_mon'].values())//len(Predict.data)] for i in Predict.data]

        # 将数据进行归一化
        self.scaler_x.fit(x)
        self.scaler_y.fit(y)
        x = self.scaler_x.transform(x)
        y = self.scaler_y.transform(y)

        # 转换为张量, list用tensor, array用from_numpy
        self.x = torch.tensor(x, dtype=torch.float32)
        self.y = torch.tensor(y, dtype=torch.float32)

    def training_model(self):
        # 训练模型
        num_epochs = 1000
        for i in range(num_epochs):
            # 前向传播
            outputs = self.linear_regression(self.x)
            loss = self.criterion(outputs, self.y)

            # 反向传播和优化
            self.optimizer.zero_grad()
            loss.backward()
            self.optimizer.step()

            # 打印训练信息
            # if (i + 1) % 100 == 0:
            #     print('loss: {}'.format(loss))

    def predict_model(self):
        pre_1 = input('请输入要预测的年份(多个用空格‘ ’隔开):\n').split(' ')
        if pre_1[-1] == ' ':
            print('请按着格式来, 前后都不能用空格')
            pre_1 = input('请输入要预测的年份(多个用空格‘ ’隔开):\n').split(' ')
        pre_1 = [int(k) for k in pre_1]
        pre_1.insert(0, 0)
        pre_data = [[i] for i in pre_1]
        # 测试模型
        with torch.no_grad():
            x = self.scaler_x.transform(pre_data)
            text = torch.tensor(x, dtype=torch.float32)
            predict = self.linear_regression(text).numpy()
        pre_2 = list(self.scaler_y.inverse_transform(predict[1:]))
        for i in pre_2:
            print(f'{pre_data[pre_2.index(i)+1][0]} 年的预测的房价价格为:\t{int(i[0])} 元')

    def save_model(self):
        self.training_model()
        with open('model.pht', 'wb')as f:
            pickle.dump(self.model, f)

    def load_model(self):
        # self.model = self.model.load_state_dict(torch.load('model.pth'))
        with open('model.pht', 'rb') as f:
            self.model = pickle.load(f)

if __name__ == '__main__':
    # 1. Get_data, 爬取数据
    get_data = Get_data()
    get_data.start()

    # 2. Predict, 训练数据, 得到线性模型, 保存模型
    pre = Predict()
    pre.get_standard_data()
    pre.training_model()

    # 3. 用得到的数据模型进行预测
    pre.predict_model()

    # pre.save_model()
    # pre.load_model()
    # pre.predict_model()



