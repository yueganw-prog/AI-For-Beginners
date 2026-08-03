"""
Phase 0 / Week 2 — Python 基础 II 参考答案
==========================================
先自己做 exercise.py, 实在卡住再看这里。
"""

# 练习 1: 词频统计器
print("=== 练习 1: 词频统计 ===")

def word_freq(text):
    result = {}
    for word in text.split():
        result[word] = result.get(word, 0) + 1
    return result

# 用 collections.Counter 的简洁写法:
# from collections import Counter
# def word_freq(text):
#     return dict(Counter(text.split()))

assert word_freq("a a b c a") == {"a": 3, "b": 1, "c": 1}
assert word_freq("") == {}
print("word_freq 全部通过!")

# 练习 2: 猜数字游戏
print("\n=== 练习 2: 猜数字 ===")

def guess_game():
    import random
    target = random.randint(1, 100)
    attempts = 0
    print("我想了一个 1-100 之间的数字, 来猜猜看吧!")
    while True:
        try:
            guess = int(input("你的猜测: "))
        except ValueError:
            print("请输入一个整数!")
            continue
        attempts += 1
        if guess < target:
            print("小了")
        elif guess > target:
            print("大了")
        else:
            print(f"猜对了! 用了 {attempts} 次 🎉")
            break

# 练习 3: 极简待办事项程序
print("\n=== 练习 3: 待办事项 ===")

def add_todo(todos, task):
    todos.append({"task": task, "done": False})


def list_todo(todos):
    for i, item in enumerate(todos):
        mark = "[x]" if item["done"] else "[ ]"
        print(f"{mark} {i}: {item['task']}")


def mark_done(todos, index):
    todos[index]["done"] = True


todos = []
add_todo(todos, "学 Python")
add_todo(todos, "跑 Notebook")
assert todos == [
    {"task": "学 Python", "done": False},
    {"task": "跑 Notebook", "done": False},
]
mark_done(todos, 0)
assert todos[0]["done"] is True
list_todo(todos)
print("add_todo / mark_done 全部通过!")

# 练习 4: 自己实现 sum_range(a, b)
print("\n=== 练习 4: sum_range ===")

def sum_range(a, b):
    total = 0
    for i in range(a, b):
        total += i
    return total

# 一行写法(配合 max 保证 a<b 时返回 0):
# def sum_range(a, b):
#     return sum(range(max(a, b - a), b)) if a < b else 0

assert sum_range(1, 5) == 10
assert sum_range(5, 5) == 0
assert sum_range(3, 2) == 0
print("sum_range 全部通过!")

# 附加题: 安全的整数读取
print("\n=== 附加题: 安全读取 ===")

def safe_int():
    while True:
        try:
            return int(input("请输入一个整数: "))
        except ValueError:
            print("输入无效, 请重试。")

print("\nWeek 2 完成!")
