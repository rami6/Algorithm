"""
Problem description
 - https://app.codility.com/programmers/lessons/5-prefix_sums/passing_cars/

score
 - 100%
"""


def solution(A):
    pass_zeros = 0
    count = 0
    for i in range(len(A)):
        if A[i] == 0:
            pass_zeros += 1
        else:
            count += pass_zeros
            if count > 1000000000:
                return -1

    return count