"""
Problem description
 - https://app.codility.com/programmers/lessons/6-sorting/triangle/

Section
 - Sorting

score
 - 81%: timeout error for input A of large negative values
"""


def solution(A):
    A.sort()
    for i in range(0, len(A)):
        for j in range(i + 1, len(A)):
            for k in range(j + 1, len(A)):
                if A[i] + A[j] > A[k]:
                    return 1
                else:
                    break
    return 0
