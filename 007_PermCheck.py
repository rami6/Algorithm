"""
Problem description
 - https://app.codility.com/programmers/lessons/4-counting_elements/perm_check/

Section
 - Counting Elements

score
 - 100%
"""

from collections import Counter


def solution(A):
    c = Counter(A)
    for i in range(1, len(A) + 1):
        if c[i] != 1:
            return 0

    return 1
