"""
Phase 0 / Week 1 — Python 基础 I 参考答案
==========================================
先自己做 exercise.py, 实在卡住再看这里。
"""

# 练习 1: 打印 1-100 的所有偶数
print("=== 练习 1: 偶数 ===")
for i in range(1, 101):
    if i % 2 == 0:
        print(i)

# 练习 2: 判断闰年
print("\n=== 练习 2: 闰年 ===")

def is_leap(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False

# 等价写法(一行):
# def is_leap(year):
#     return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

assert is_leap(2000) is True
assert is_leap(1900) is False
assert is_leap(2020) is True
assert is_leap(2019) is False
print("is_leap 全部通过!")

# 练习 3: 列表去重(保持顺序)
print("\n=== 练习 3: 列表去重 ===")

def unique(lst):
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result

# 更简洁的写法(用集合做去重, 但集合无序, 需配合顺序):
# def unique(lst):
#     seen = set()
#     result = []
#     for item in lst:
#         if item not in seen:
#             seen.add(item)
#             result.append(item)
#     return result

assert unique([1, 2, 2, 3, 3, 3]) == [1, 2, 3]
assert unique(["a", "b", "a", "c"]) == ["a", "b", "c"]
assert unique([]) == []
print("unique 全部通过!")

# 练习 4: 统计元音字母个数(不区分大小写)
print("\n=== 练习 4: 元音统计 ===")

def count_vowels(s):
    vowels = "aeiou"
    count = 0
    for ch in s.lower():
        if ch in vowels:
            count += 1
    return count

assert count_vowels("hello") == 2
assert count_vowels("AEIOU") == 5
assert count_vowels("xyz") == 0
print("count_vowels 全部通过!")

print("\n全部完成! 恭喜你完成 Week 1")
