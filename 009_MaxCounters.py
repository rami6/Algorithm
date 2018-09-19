"""
Problem description
 - https://app.codility.com/programmers/lessons/4-counting_elements/max_counters/

score
 - 66%
"""


def solution(N, A):
    counter = [0] * N
    for num in A:
        if num <= N:
            counter[num - 1] += 1
        else:
            counter = [max(counter)] * N

    return counter