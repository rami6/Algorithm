"""
Problem description
 - https://app.codility.com/programmers/lessons/6-sorting/triangle/

Section
 - Sorting

score
 - 100%
"""


def solution(A):
    A.sort()
    for i in range(0, len(A)):
        if A[i] > 0:
            for j in range(i + 1, len(A)):
                for k in range(j + 1, len(A)):
                    if A[i] + A[j] > A[k]:
                        return 1
                    else:
                        break
    return 0
