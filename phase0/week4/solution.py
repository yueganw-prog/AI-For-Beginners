"""
Phase 0 / Week 4 — 综合练习参考答案
===================================
"""

import numpy as np

scores = {
    "Alice": [88, 92, 79],
    "Bob": [70, 85, 90],
    "Carol": [95, 89, 94],
    "David": [60, 66, 72],
}
SUBJECTS = ["Math", "English", "Science"]


def student_average(scores, name):
    return np.mean(scores[name])


def subject_average(scores, index):
    return np.mean([scores[name][index] for name in scores])


def best_student(scores):
    best_name = None
    best_avg = -1
    for name in scores:
        avg = student_average(scores, name)
        if avg > best_avg:
            best_avg = avg
            best_name = name
    return best_name, best_avg


def grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    else:
        return "D"


if __name__ == "__main__":
    for name in scores:
        avg = student_average(scores, name)
        print(f"{name}: 平均分 {avg:.1f} -> 等级 {grade(avg)}")

    for i, subj in enumerate(SUBJECTS):
        print(f"班级{subj}平均分: {subject_average(scores, i):.1f}")

    name, avg = best_student(scores)
    print(f"全班最高: {name}, 平均分 {avg:.1f}")
