"""
Phase 0 / Week 1 — Python 基础 I 练习
=======================================
运行方式: 在命令行或 IDE 中执行  python exercise.py
每个练习下方有 TODO 提示, 把代码填在标记处。
写完后可以和 solution.py 对照。
"""

# ---------------------------------------------------------------
# 练习 1: 打印 1-100 的所有偶数
# 要求: 用 for 循环 + range() 遍历 1 到 100,
#       只打印偶数(能被 2 整除), 每行一个。
# ---------------------------------------------------------------
print("=== 练习 1: 偶数 ===")
# TODO: 在这里写你的代码
# 提示: for i in range(1, 101): ...
for i in range(1,101):
    if(i % 2 == 0):
        print(i)



# ---------------------------------------------------------------
# 练习 2: 判断闰年
# 要求: 写一个函数 is_leap(year), 闰年返回 True, 否则返回 False。
#       闰年规则: 能被 4 整除, 但不能被 100 整除;
#       或者能被 400 整除。
# ---------------------------------------------------------------
print("\n=== 练习 2: 闰年 ===")

def is_leap(year):
    # TODO: 在这里写你的代码, 并 return True/False
    if((year % 4 == 0 and year % 100 != 0) or year%400==0):
        return True
    else:
        return False


# 测试: 下面这些断言通过说明函数写对了
assert is_leap(2000) is True   # 能被 400 整除
assert is_leap(1900) is False  # 能被 100 整除但不能被 400
assert is_leap(2020) is True   # 能被 4 整除但不能被 100
assert is_leap(2019) is False  # 不能被 4 整除
print("is_leap 全部通过!")


# ---------------------------------------------------------------
# 练习 3: 列表去重
# 要求: 写一个函数 unique(lst), 返回去掉重复元素后的新列表,
#       保持原有顺序。
# ---------------------------------------------------------------
print("\n=== 练习 3: 列表去重 ===")

def unique(lst):
    # TODO: 在这里写你的代码, 并 return 新列表
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result


assert unique([1, 2, 2, 3, 3, 3]) == [1, 2, 3]
assert unique(["a", "b", "a", "c"]) == ["a", "b", "c"]
assert unique([]) == []
print("unique 全部通过!")


# ---------------------------------------------------------------
# 练习 4: 统计元音字母个数
# 要求: 写一个函数 count_vowels(s), 返回字符串 s 中元音
#       (a e i o u, 不区分大小写)出现的次数。
# ---------------------------------------------------------------
print("\n=== 练习 4: 元音统计 ===")

def count_vowels(s):
    # TODO: 在这里写你的代码, 并 return 个数
    vowels = "aeiou"
    count=0
    for ch in s.lower():
        if ch in vowels:
            count+=1
    return count


assert count_vowels("hello") == 2   # e, o
assert count_vowels("AEIOU") == 5   # 大写也算
assert count_vowels("xyz") == 0
print("count_vowels 全部通过!")


print("\n全部练习完成! 恭喜你完成 Week 1")
