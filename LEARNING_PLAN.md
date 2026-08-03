# AI-For-Beginners 学习计划

> 目标：为找 AI 相关工作打基础，并为后续学习大模型/GenAI 做准备
> 框架：PyTorch　|　投入：每周 5-10 小时　|　基础：编程零基础
> 仓库：microsoft/AI-For-Beginners（fork：yueganw-prog/AI-For-Beginners）

## 每课固定学习流程

```
课前测验 → 通读理论 → 运行 PyTorch Notebook → 完成挑战 → 课后测验 → 做 Lab
```

## 说明

- 本课程默认你会 Python，因此 Phase 0 先补 Python/NumPy/Jupyter/git 基础。
- 课程目录里有 50+ 语言翻译，学习时可用 `translations/zh-CN/lessons/` 对照中文。
- 建议边学边在本仓库写公开学习笔记，作为求职时的学习证据。
- 找 AI 工作仅靠本课程不够，Phase 6 后需衔接大模型、Kaggle、算法题。

---

## Phase 0：Python 与工具基础（第 1-4 周，约 30 小时）

### Week 1 — Python 基础 I（约 7 小时）

语法：变量与类型（int、float、str、bool）、运算符、`if/elif/else`、`for/while`、`range`、列表 list。

练习（`phase0/week1/`）：
1. 打印 1-100 的所有偶数
2. 判断闰年函数
3. 列表去重函数
4. 统计字符串中元音字母个数

资源：Python 官方教程前 3 节 / 《Python Crash Course》ch1-5

### Week 2 — Python 基础 II（约 8 小时）

语法：字典 dict、集合 set、函数与参数、字符串方法、文件读写、`try/except`。

练习（`phase0/week2/`）：
1. 词频统计器（读 txt 文件统计单词出现次数）
2. 猜数字游戏（random）
3. 极简待办事项程序（列表+字典+循环）
4. 自己实现 `sum_range(a, b)`

资源：《Python Crash Course》ch6-10

### Week 3 — NumPy + Matplotlib（约 9 小时）⭐ 通往 ML 的桥梁

NumPy：`ndarray`、形状、索引/切片、`zeros/ones/reshape`、矩阵运算 `dot`/转置/广播。
Matplotlib：折线图、散点图、直方图。

练习（`phase0/week3/`）：
1. 用 NumPy 生成数据并计算均值/方差
2. 用矩阵公式实现最小二乘线性回归（`w = (XᵀX)⁻¹Xᵀy`）
3. 手写 2 层小网络的前向传播（纯 NumPy 矩阵乘法）
4. 画 sin/cos 曲线

资源：NumPy 官方 quickstart、Matplotlib 官方入门

### Week 4 — Jupyter + git + 小结项目（约 6 小时）

- Jupyter：markdown cell、快捷键、导出
- git：`clone/add/commit/push/status/log`
- 小结项目（`phase0/week4/student_analysis.ipynb`）：学生成绩分析 notebook

**Phase 0 完成标准**：能独立写 30-50 行脚本；会用 NumPy 做矩阵运算；能在 Jupyter 边写说明边跑代码；会 `git push` 到自己的 fork。

---

## Phase 1：课程搭建 + AI 入门 + 符号AI（第 5-7 周）

| 周 | 章节 | 任务 |
|---|---|---|
| 5 | Lesson 0 课程搭建 | conda 建环境、装依赖；PyTorch 需单独安装 |
| 5-6 | Lesson 1 引言与 AI 历史 | 通读 + 画 AI 概念脑图 |
| 6-7 | Lesson 2 知识表示/专家系统 | 跑 `Animals.ipynb`、`FamilyOntology.ipynb` |

环境关键点：
- requirements.txt 已含 TensorFlow 等；PyTorch 按官网命令单独安装。
- 仓库体积较大（含 translations），本机克隆已完整；如需瘦身可用 sparse checkout 排除 `translations`、`translated_images`。

---

## Phase 2：神经网络核心（第 8-11 周）⭐ 最重要，放慢脚步

| 周 | 章节 | 任务 |
|---|---|---|
| 8 | Lesson 3 感知机 | 跑 `Perceptron.ipynb`，理解权重/偏置/激活 |
| 9 | Lesson 4 MLP + 自建框架 | 亲手实现 `OwnFramework.ipynb` |
| 10-11 | Lesson 5 PyTorch + 过拟合 | 跑 `IntroPyTorch.ipynb`，吃透损失/优化器/反向传播 |

**完成标准**：能不看代码讲清"神经网络如何通过反向传播更新权重"。

---

## Phase 3：计算机视觉（第 12-17 周）

| 周 | 章节 | 备注 |
|---|---|---|
| 12 | L6 OpenCV 入门 | 图像读写 |
| 13-14 | L7 CNN + 架构 | 跑 `ConvNetsPyTorch.ipynb` |
| 15 | L8 迁移学习 ⭐ | 求职最实用，跑 `TransferLearningPyTorch.ipynb` + Lab |
| 16 | L9-10 自编码器/GAN | 跑通了解即可 |
| 17 | L11-12 目标检测/分割 | 了解原理 |

---

## Phase 4：自然语言处理（第 18-23 周）⭐ 与大模型最相关

| 周 | 章节 | 备注 |
|---|---|---|
| 18 | L13 BOW/TF-IDF | 跑 PyTorch notebook |
| 19 | L14 词嵌入 Word2Vec/GloVe | `EmbeddingsPyTorch.ipynb` |
| 20 | L15 语言建模 CBoW | `CBoW-PyTorch.ipynb` |
| 21 | L16-17 RNN/生成式 RNN | 理解 LSTM/GRU |
| 22 | L18 Transformer/BERT ⭐ | `TransformersPyTorch.ipynb`，吃透 attention |
| 23 | L19-20 NER + LLM/Prompt/Few-shot | L20 是大模型桥梁 |

---

## Phase 5：其他 AI 技术 + 伦理（第 24-25 周）

| 周 | 章节 | 备注 |
|---|---|---|
| 24 | L21 遗传算法 + L22 强化学习 | 跑 `CartPole-RL-PyTorch.ipynb`（最有趣） |
| 25 | L23 多智能体 + L24 AI 伦理 | 通读理论，了解 Responsible AI |

---

## Phase 6：衔接大模型/GenAI（第 26 周起）

- 转 **microsoft/Generative-AI-for-Beginners**：LLM、Prompt、RAG、Fine-tuning。
- 做 1 个完整项目写进简历（LLM+RAG 问答应用 或 微调小模型）。
- 参加 1-2 个 Kaggle 入门比赛。

---

## 求职补充建议（贯穿全程）

1. 每课结束在 GitHub 写一篇 Markdown 总结笔记，公开到本仓库。
2. 数学短板用 3Blue1Brown《线性代数的本质》+《深度学习》(Goodfellow) 补齐，只补够用。
3. 每阶段做一个迷你项目（CV 迁移学习分类、NLP 情感分析等）。
4. 后期每周刷 3-5 道 LeetCode 算法题。
5. 中文对照：`translations/zh-CN/lessons/`。

---

## 里程碑检查点

- 第 11 周结束：能讲清神经网络原理 + 会用 PyTorch 训练简单模型 ✅
- 第 17 周结束：能迁移学习做图像分类 ✅
- 第 23 周结束：理解 Transformer，能跑通 BERT/LLM Notebook ✅
- 第 26 周结束：具备转向大模型学习的完整基础 ✅
