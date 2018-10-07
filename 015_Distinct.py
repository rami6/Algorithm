"""
Problem description
 - https://app.codility.com/programmers/lessons/6-sorting/distinct/

Section
 - Sorting

score
 - 100%
"""


def solution(A):
    if len(A) == 0:
        return 0

    count = 1
    A.sort()
    for i in range(1, len(A)):
        if A[i] != A[i - 1]:
            count += 1

    return count