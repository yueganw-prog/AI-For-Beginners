"""
Phase 0 / Week 3 — NumPy + Matplotlib 练习
===========================================
运行方式: python exercise.py
需要先安装依赖:  pip install numpy matplotlib
如果还没装, 打开命令行执行上面的命令再运行。
写完后对照 solution.py。
"""

import numpy as np

# ---------------------------------------------------------------
# 练习 1: 均值与方差
# 要求: 写一个函数 stats(data), 输入一维数组,
#       返回 (mean, variance), 均值用 np.mean, 方差用 np.var。
# ---------------------------------------------------------------
print("=== 练习 1: 均值与方差 ===")

def stats(data):
    # TODO: 在这里写你的代码, 并 return (mean, variance)
    mean = np.mean(data)
    variance = np.var(data)
    return (mean, variance) 



assert np.isclose(stats([1, 2, 3, 4])[0], 2.5)
assert np.isclose(stats([1, 2, 3, 4])[1], 1.25)
print("stats 全部通过!")


# ---------------------------------------------------------------
# 练习 2: 最小二乘线性回归
# 要求: 已知 X(形状 N x 2, 第一列全 1 作截距)和 y(长度 N),
#       用矩阵公式 w = (XᵀX)⁻¹Xᵀy 求出系数 w(长度为 2)。
#       提示: np.linalg.inv 求逆, np.dot 或 @ 做矩阵乘法。
# ---------------------------------------------------------------
print("\n=== 练习 2: 线性回归 ===")

def least_squares(X, y):
    # TODO: 在这里写你的代码, 并 return w
    w = np.linalg.inv(X.T @ X) @ X.T @ y
    return w


# 造数据: y = 2 + 3x
X = np.column_stack([np.ones(10), np.arange(10)])
y = 2 + 3 * np.arange(10)
w = least_squares(X, y)
assert np.allclose(w, [2, 3]), f"期望 [2, 3], 得到 {w}"
print("least_squares 全部通过!")


# ---------------------------------------------------------------
# 练习 3: 两层网络的前向传播
# 要求: 实现一个两层全连接网络的前向传播(纯 NumPy)。
#       输入 x(长度 D), 权重 W1(D x H)、b1(H), W2(H x O)、b2(O),
#       隐藏层用 tanh 激活, 输出层无激活。
#       返回网络的输出(长度 O)。
# ---------------------------------------------------------------
print("\n=== 练习 3: 前向传播 ===")

def forward(x, W1, b1, W2, b2):
    # TODO: 在这里写你的代码
    # 第 1 步: h = np.tanh(x @ W1 + b1)
    # 第 2 步: return h @ W2 + b2
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


# ---------------------------------------------------------------
# 练习 4: 画 sin / cos 曲线
# 要求: 用 np.linspace 生成 x 从 -π 到 π 的 100 个点,
#       画 y1 = sin(x) 和 y2 = cos(x) 两条曲线, 加图例,
#       并调用 plt.show() 显示。
# ---------------------------------------------------------------
print("\n=== 练习 4: sin/cos 曲线 ===")

def plot_sin_cos():
    import matplotlib.pyplot as plt
    # TODO: 在这里写你的代码
    # 提示:
    #   x = np.linspace(-np.pi, np.pi, 100)
    #   plt.plot(x, np.sin(x), label="sin")
    #   plt.plot(x, np.cos(x), label="cos")
    #   plt.legend(); plt.show()
    x = np.linspace(-np.pi, np.pi, 100)
    plt.plot(x, np.sin(x), label="sin")
    plt.plot(x, np.cos(x), label="cos")
    plt.legend()
    plt.show()


# 取消下面这行的注释会弹出绘图窗口:
plot_sin_cos()

print("\nWeek 3 练习完成!")
