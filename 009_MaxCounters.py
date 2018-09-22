"""
Problem description
 - https://app.codility.com/programmers/lessons/4-counting_elements/max_counters/

score
 - 66%
"""

# correct, but timeout error for a few test cases


def solution(N, A):
    counter = [0] * N
    base = 0

    for num in A:
        if num != N + 1:
            counter[num] += 1
        else:
            base += max(counter)
            counter = [0] * N

    for i in range(len(counter)):
        counter[i] += base

    return counter




solution(5, [6, 6, 6, 6, 6, 6])