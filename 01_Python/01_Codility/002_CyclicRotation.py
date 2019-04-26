"""
Problem description
 - https://app.codility.com/programmers/lessons/2-arrays/cyclic_rotation/

Section
 - Arrays

score
 - 100%
"""


def solution(A, K):
    if len(A) == 0:
        return A

    new_arr = []
    prev_arr = A
    for i in range(K):
        new_arr.append(prev_arr[-1])
        for j in range(len(A) - 1):
            new_arr.append(prev_arr[j])
        prev_arr = new_arr
        new_arr = []

    return prev_arr