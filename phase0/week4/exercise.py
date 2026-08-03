"""
Phase 0 / Week 4 — 综合练习: 学生成绩分析(脚本版)
=================================================
本章把前几周的知识(列表、字典、函数、NumPy)串起来。
真正的"小结项目"请使用 student_analysis.ipynb(带 markdown 说明)。
先做 exercise.py, 再对照 solution.py。
"""

import numpy as np

# 班级成绩数据: 键是学生名, 值是三门课 [数学, 英语, 科学] 的成绩
scores = {
    "Alice": [88, 92, 79],
    "Bob": [70, 85, 90],
    "Carol": [95, 89, 94],
    "David": [60, 66, 72],
}
SUBJECTS = ["Math", "English", "Science"]


# ---------------------------------------------------------------
# 任务 1: 单个学生的平均分
# 要求: student_average(scores, name) 返回该学生三门课的平均分(float)。
# ---------------------------------------------------------------
def student_average(scores, name):
    # TODO: 用 np.mean 或手动求和计算
    pass


assert np.isclose(student_average(scores, "Alice"), (88 + 92 + 79) / 3)
print("task 1 通过!")


# ---------------------------------------------------------------
# 任务 2: 每门课的班级平均分
# 要求: subject_average(scores, index) 返回第 index 门课的班级平均分。
#       比如 index=0 表示所有学生的"数学"成绩的平均。
# ---------------------------------------------------------------
def subject_average(scores, index):
    # TODO: 收集所有学生第 index 门课的成绩, 再求平均
    pass


assert np.isclose(subject_average(scores, 0), (88 + 70 + 95 + 60) / 4)
print("task 2 通过!")


# ---------------------------------------------------------------
# 任务 3: 找出平均分最高的学生
# 要求: best_student(scores) 返回 (姓名, 平均分)。
#       提示: 可以复用 task 1 的 student_average。
# ---------------------------------------------------------------
def best_student(scores):
    # TODO: 遍历所有学生, 找出平均分最高的
    pass


name, avg = best_student(scores)
assert name == "Carol" and np.isclose(avg, (95 + 89 + 94) / 3)
print("task 3 通过!")


# ---------------------------------------------------------------
# 任务 4: 按平均分划分等级
# 要求: grade(avg) 返回:
#       avg >= 90 -> "A", >= 80 -> "B", >= 70 -> "C", 否则 -> "D"
# ---------------------------------------------------------------
def grade(avg):
    # TODO: 实现等级判断
    pass


assert grade(95) == "A"
assert grade(84) == "B"
assert grade(72) == "C"
assert grade(50) == "D"
print("task 4 通过!")


print("\nWeek 4 脚本版练习完成! 接下来打开 student_analysis.ipynb 做小结项目")
