import numpy as np


score = np.array(
    [[1, 2, 3, 4, 5, 6, 7, 8],
    [1, 2, 3, 4, 5, 6, 7, 8],
    [1, 2, 3, 4, 5, 6, 7, 8],
    [1, 2, 3, 4, 5, 6, 7, 8]]
)

score += 10
print(score)

score = np.array([1, 2, 3, 4, 5, 6, 7, 8])

print(score.dtype)

score = np.ones([4, 8])
print(score)

print(np.zeros([4, 8]))

print(np.logspace(0, 4, 5, base=3))

ran_1 = np.random.randn(5)
print(ran_1)

x_1 = np.random.normal(0, 1, size=10000)

print(x_1)


