import torch
text = '你好啊！'
data = torch.tensor(text.encode('utf-8'), dtype=torch.long)

print(data.shape, data.dtype)
print(data)
