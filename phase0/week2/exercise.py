"""
Phase 0 / Week 2 — Python 基础 II 练习
=======================================
运行方式: python exercise.py
练习包含字典、集合、函数、文件读写、异常。
每个练习把代码填在 TODO 处, 写完后对照 solution.py。
"""

# ---------------------------------------------------------------
# 练习 1: 词频统计器
# 要求: 写一个函数 word_freq(text), 输入一段文本字符串,
#       返回一个字典, key 是单词, value 是该单词出现的次数。
#       提示: 用 text.split() 按空白切分即可(暂不处理标点)。
# ---------------------------------------------------------------
print("=== 练习 1: 词频统计 ===")

def word_freq(text):
    # TODO: 在这里写你的代码, 并 return 字典
    result = {}
    for word in text.split():
        if word in result:
            result[word] += 1
        else:
            result[word] = 1
    return result

assert word_freq("a a b c a") == {"a": 3, "b": 1, "c": 1}
assert word_freq("") == {}
print("word_freq 全部通过!")


# ---------------------------------------------------------------
# 练习 2: 猜数字游戏
# 要求: 用 random.randint(1, 100) 生成一个 1-100 的随机数,
#       让用户循环输入猜测, 提示"大了"/"小了", 猜中后结束
#       并打印猜的次数。
# 提示: 用 input() 读用户输入, 用 int() 转成整数。
#       这个练习无法用断言测试, 直接运行交互体验。
# ---------------------------------------------------------------
print("\n=== 练习 2: 猜数字 ===")

def guess_game():
    import random
    target = random.randint(1, 100)
    # TODO: 在这里写游戏逻辑
    attempts = 0
    print("我想了一个 1-100 之间的数字, 来猜吧")

    while True:
        guess = int(input("请输入你猜的数字 (1-100): "))
        attempts += 1
        if guess < target:
            print("小了")
        elif guess > target:
            print("大了")
        else:
            print(f"恭喜你，猜对了！总共猜了 {attempts} 次。")
            break


# 取消下面这行的注释即可游玩(也可以在命令行单独运行本文件体验):
# guess_game()


# ---------------------------------------------------------------
# 练习 3: 极简待办事项程序
# 要求: 用一个列表存放待办事项(每个事项是字典 {"task": str, "done": bool}),
#       实现 add_todo(todos, task) 添加、list_todo(todos) 打印、
#       mark_done(todos, index) 按序号标记完成。
# ---------------------------------------------------------------
print("\n=== 练习 3: 待办事项 ===")

def add_todo(todos, task):
    # TODO: 往 todos 里追加 {"task": task, "done": False}
    todos.append({"task": task, "done": False})


def list_todo(todos):
    # TODO: 逐行打印, 已完成加 [x], 未完成加 [ ]
    for i, todo in enumerate(todos):
        status = "x" if todo["done"] else "[]"
        print(f"[{status}] {todo['task']}")


def mark_done(todos, index):
    # TODO: 把第 index 项(从 0 开始)的 done 设为 True
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


# ---------------------------------------------------------------
# 练习 4: 自己实现 sum_range(a, b)
# 要求: 写一个函数 sum_range(a, b), 返回 a 到 b 之间所有整数的和
#       (含 a, 不含 b)。若 a >= b 返回 0。
# ---------------------------------------------------------------
print("\n=== 练习 4: sum_range ===")

def sum_range(a, b):
    # TODO: 在这里写你的代码, 并 return 结果
    result = 0
    for i in range(a, b):
        if a >= b:
            return 0
        result += i
    return result


assert sum_range(1, 5) == 10     # 1+2+3+4
assert sum_range(5, 5) == 0
assert sum_range(3, 2) == 0
print("sum_range 全部通过!")


# ---------------------------------------------------------------
# 附加题(选做): 安全的整数读取
# 写一个 safe_int() 函数, 用 input() 读取输入并转成整数,
# 如果输入不是数字就用 try/except 捕获异常并提示重新输入。
# ---------------------------------------------------------------
print("\n=== 附加题: 安全读取(选做) ===")

def safe_int():
    # TODO: 用 try/except + while 实现
    print("请安全输入一个整数:")
    while True:
        try:
            user_input = input() # 读取用户输入
            value = int(user_input) # 转成整数
            return value # 返回整数
        
        except ValueError: # 输入不是整数
            print("输入无效，请输入一个整数:") # 提示用户重新输入
            continue # 继续循环, 重新输入
        except KeyboardInterrupt: # 用户按 Ctrl+C 取消输入
            print("用户取消输入") # 提示用户取消输入
            return None # 返回 None 表示用户取消输入

# 取消注释体验:
n = safe_int() 
print("你输入了:", n)

print("\nWeek 2 练习完成!")
