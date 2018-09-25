"""
Problem description
 - https://app.codility.com/programmers/lessons/4-counting_elements/missing_integer/

score
 - 66%
"""

# Correct, but poor efficiency

def solution(A):
    i = 1
    while i <= max(A):
        if not i in A:
            return i
        i += 1

    return i
