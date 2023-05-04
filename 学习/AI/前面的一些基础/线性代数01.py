import torch

A = torch.arange(20).reshape(4, 5)
print(A)

B = A.T
print(B)

C = torch.tensor([[1, 2, 3], [2, 0, 4], [3, 4, 5]])
print(C == C.T)

X = torch.arange(24).reshape(2, 3, 4)
print(X)

A = torch.arange(20, dtype=torch.float32).reshape(5, 4)
B = A.clone()
print(A)

x = torch.arange(4, dtype=torch.float32)
print(x.sum())

print(A.sum(axis=0))
print(A.sum(axis=1))

print(A.mean())
print(A.sum() / A.numel())

print(A.mean(axis=0))

print(A.sum(axis=1, keepdims=True))
print(A.sum(axis=0, keepdims=True))

sum_A = A.sum(axis=1, keepdims=True)
print(A / sum_A)

a = torch.arange(4, dtype=torch.float32)
b = torch.ones(4, dtype=torch.float32)

print('*'*20)
print(a)
print(b)
print(torch.dot(a, b))
print(sum(a*b))

print('#'*20)
x = torch.arange(4, dtype=torch.float32)
print(A.shape)
print(x)
print(A)
print(torch.mv(A, x))

print('&'*20)
C = torch.arange(8, dtype=torch.float32).reshape(2, 4)
D = torch.ones(8, dtype=torch.float32).reshape(4, 2)
print(C)
print(D)
print(torch.mm(C, D))

print('^'*20)
u = torch.tensor([3.0, -4.0])
print(torch.norm(u))
print(torch.abs(u))
