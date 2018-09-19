"""
Problem description
 - https://app.codility.com/programmers/lessons/4-counting_elements/frog_river_one/

score
 - 72%
"""


def solution(X, A):
    pos = [0] * X
    for i, num in enumerate(A):
        if num <= X:
            pos[num - 1] += 1
        if not 0 in pos:
            return i

    return -1
