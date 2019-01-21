"""
Problem description
 - https://app.codility.com/programmers/lessons/4-counting_elements/missing_integer/

Section
 - Counting Elements

score
 - 100%
"""


def solution(A):
    # Check if 1 should be returned.
    if 1 not in A:
        return 1

    # Check the case the length of A is 1 and the condition above is not applicable.
    if A == [1]:
        return 2

    # Check other cases.
    A.sort()

    i = 0
    while i < len(A) - 1:
        if A[i] >= 0 and A[i + 1] - A[i] > 1:
            return A[i] + 1
        i += 1

    return A[len(A) - 1] + 1