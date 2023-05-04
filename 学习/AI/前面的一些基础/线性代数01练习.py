import torch

A = torch.arange(16, dtype=torch.float32).reshape(4, 4)
B = torch.ones(16, dtype=torch.float32).reshape(4, 4)
print(A)
print(B)

C = A.T + B.T
print(C)
print((A + B).T)

print('*'*30)
print(A + A.T)
print(A)

print(torch.norm(B))
print(torch.norm(A))

