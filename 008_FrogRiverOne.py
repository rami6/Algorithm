"""
Problem description
 - https://app.codility.com/programmers/lessons/4-counting_elements/frog_river_one/

score
 - 100%
"""


def solution(X, A):
    positions = {}
    for i, num in enumerate(A):
        if num in positions.keys():
            pass
        else:
            positions[num] = i

    max_pos = 0
    for j in range(1, X + 1):
        if not j in positions.keys():
            return -1

        max_pos = max(max_pos, positions[j])

    return max_pos
