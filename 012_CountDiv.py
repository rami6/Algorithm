"""
Problem description
 - https://app.codility.com/programmers/lessons/5-prefix_sums/count_div/

score
 - 100%
"""


def solution(A, B, K):
    start = A

    while start % K != 0:
        start += 1
        if start > B:
            return 0

    new_B = B - start

    return new_B // K + 1