"""
Problem description
 - https://app.codility.com/programmers/lessons/4-counting_elements/max_counters/

Section
 - Counting Elements

score
 - 100%
"""


def solution(N, A):
    counter = [0] * N
    base = 0
    base_current = 0

    for num in A:
        if num != N + 1:
            if counter[num - 1] < base:
                counter[num - 1] = base
            counter[num - 1] += 1
            if base_current < counter[num - 1]:
                base_current = counter[num - 1]
        else:
            base = base_current

    for i in range(0, N):
        if counter[i] < base:
            counter[i] = base

    return counter
