"""
Problem description
 - https://app.codility.com/programmers/lessons/3-time_complexity/frog_jmp/

score
 - 100%
"""


def solution(X, Y, D):
    distance = Y - X
    if distance % D == 0:
        return distance // D
    else:
        return distance // D + 1
