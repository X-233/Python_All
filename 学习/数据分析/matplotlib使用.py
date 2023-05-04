import matplotlib.pyplot as plt
import random
import re
# plt.rcParams['font.sans-serif'] = ['KaiTi']
# plt.rcParams['axes.unicode_minus'] = False
#
# plt.figure(figsize=(20, 8), dpi=200)
#
#
# x = [i for i in range(60)]
# y = [random.uniform(15, 24) for i in x]
# y1 = [random.uniform(4, 10) for i in x]
# plt.plot(x, y, color='red')
# plt.plot(x, y1, color='blue')
# plt.legend(loc='upper left')
#
# x_1 = [f'11点{i}分' for i in x]
# y_1 = [i for i in range(40)]
#
# plt.xticks(x[::5], x_1[::5])
# plt.yticks(y_1[::5])
#
# plt.grid(linestyle='--')
# plt.xlabel('时间/分', fontsize=20)
# plt.ylabel('温度/C', fontsize=20)
# plt.title('折线图', fontsize=20)
#
# plt.savefig('添加背景.png')
# plt.show()
# plt.close()
str_1 = '你好_1l23.f.er.jpg'
str_2 = '你好1l23.f.er.jpg'
str_3 = '你好.jpg'

data = re.sub(r'[\d+|_]', '', str_1)

s = '你好_1l23.f.er.jpg'
s = re.sub(r'[_|\d+].*\.', '.', s)
print(type(s))
print(data)

str_3 = "{'name': '微信8.029-净化2.6.6-原始微信权限_使用TrollStore安装支持voip_正常跳转_正常分享组件功能_官替.ipa', 'size': 269160968, 'is_dir': False, 'modified': '2022-10-04T06:50:04.877Z', 'sign': 'MGxZddTRJGvfl2U6mS0bQfCSSTkeYWZnQX60prRC0m0=:0', 'thumb': '', 'type': 0, 'path_1': '/IOS资源/应用/微信QQ抖音等常用应用/微信/微信8.029-净化2.6.6-原始微信权限_使用TrollStore安装支持voip_正常跳转_正常分享组件功能_官替.ipa'}"
str_3 = eval(str_3)


with open('苹果软件列表_1.txt', 'r', encoding='utf-8')as f:
    file = [i.strip() for i in f.readlines()]

# file.sort(key=lambda key: key['size'], reverse=True)
file = list(set(file))
x_data =[eval(i)['name'] for i in file]
y_data =[eval(i)['size'] for i in file]
x_data1 = [re.sub(r'[_|\d+].*\.', '.', i) for i in x_data]
print(x_data1[:10])

plt.xticks(x_data, x_data1)
plt.barh(x_data[:10:1], y_data[:10:1], label='大小', color='red', height=0.1)