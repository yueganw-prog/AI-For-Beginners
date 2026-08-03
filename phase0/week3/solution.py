"""
Phase 0 / Week 3 — NumPy + Matplotlib 参考答案
==============================================
先自己做 exercise.py, 实在卡住再看这里。
"""

import numpy as np

# 练习 1: 均值与方差
print("=== 练习 1: 均值与方差 ===")

def stats(data):
    arr = np.asarray(data, dtype=float)
    return np.mean(arr), np.var(arr)

assert np.isclose(stats([1, 2, 3, 4])[0], 2.5)
assert np.isclose(stats([1, 2, 3, 4])[1], 1.25)
print("stats 全部通过!")

# 练习 2: 最小二乘线性回归 w = (XᵀX)⁻¹Xᵀy
print("\n=== 练习 2: 线性回归 ===")

def least_squares(X, y):
    XT_X = X.T @ X
    XT_y = X.T @ y
    return np.linalg.inv(XT_X) @ XT_y

X = np.column_stack([np.ones(10), np.arange(10)])
y = 2 + 3 * np.arange(10)
w = least_squares(X, y)
assert np.allclose(w, [2, 3]), f"期望 [2, 3], 得到 {w}"
print("least_squares 全部通过! 截距 =", w[0], "斜率 =", w[1])

# 练习 3: 两层网络前向传播
print("\n=== 练习 3: 前向传播 ===")

def forward(x, W1, b1, W2, b2):
    h = np.tanh(x @ W1 + b1)
    return h @ W2 + b2

np.random.seed(0)
x = np.array([1.0, 2.0])
W1 = np.random.randn(2, 3)
b1 = np.zeros(3)
W2 = np.random.randn(3, 1)
b2 = np.zeros(1)
out = forward(x, W1, b1, W2, b2)
print("输出形状:", out.shape, "数值:", out)
assert out.shape == (1,)
print("forward 运行成功!")

# 练习 4: 画 sin / cos 曲线
print("\n=== 练习 4: sin/cos 曲线 ===")

def plot_sin_cos():
    import matplotlib.pyplot as plt
    x = np.linspace(-np.pi, np.pi, 100)
    plt.plot(x, np.sin(x), label="sin")
    plt.plot(x, np.cos(x), label="cos")
    plt.legend()
    plt.grid(True)
    plt.show()

# 想看到图形时取消注释:
# plot_sin_cos()

print("Week 3 完成!")
