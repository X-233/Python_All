"""
计算 0 ~ 100 之间 所有 偶数 的累计求和结果

开发步骤

1. 编写循环确认要计算的数字
2. 添加结果变量，在循环内部处理计算结果
"""
"""自己在下方编写代码实现功能"""
# 1
sum_1 = sum([i for i in range(0, 101, 2)])
print(sum_1)

# 2
sum_2 = 0
for i in range(101):
    if i % 2 == 0:
        sum_2 += i
print(sum_2)