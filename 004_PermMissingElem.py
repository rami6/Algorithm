"""
Problem description
 - https://app.codility.com/programmers/lessons/3-time_complexity/perm_missing_elem/

score
 - 100%
"""


def solution(A):
    A.sort()
    for i in range(len(A)):
        if A[i] != i + 1:
            return i + 1

    return len(A) + 1
