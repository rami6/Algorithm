"""
Problem description
 - https://app.codility.com/programmers/lessons/5-prefix_sums/count_div/

score
 - 50% ...correct, but less efficient
"""


def solution(A, B, K):
    count = 0
    for num in range(A, B + 1):
        if num % K == 0:
            count += 1

    return count