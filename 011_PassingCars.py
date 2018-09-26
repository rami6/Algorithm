"""
Problem description
 - https://app.codility.com/programmers/lessons/5-prefix_sums/passing_cars/

score
 - 50%
"""

# Correct, but less efficient


def solution(A):
    if len(A) == 1:
        return 0

    count = 0
    for i in range(len(A) - 1):
        if A[i] == 0:
            count += A[i + 1:].count(1)

    return count