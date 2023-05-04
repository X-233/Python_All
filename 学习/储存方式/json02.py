import json

data = {
    'name': '张三',
    'age': 24,
}

# ensure_ascii=False, 不使用默认编码
data_1 = json.dumps(data, ensure_ascii=False)
print(data_1)
