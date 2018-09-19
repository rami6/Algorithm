"""
Problem description
 - https://app.codility.com/programmers/lessons/3-time_complexity/tape_equilibrium/

score
 - 100%
"""


def solution(A):
    left = A[0]
    right = sum(A[1:])
    minimum = abs(left - right)

    if len(A) == 2:
        return abs(left - right)

    for i in range(1, len(A) - 1):
        left += A[i]
        right -= A[i]
        minimum = min(minimum, abs(left - right))

    return minimum