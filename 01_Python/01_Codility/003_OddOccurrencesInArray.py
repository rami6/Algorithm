"""
Problem description
 - https://app.codility.com/programmers/lessons/2-arrays/odd_occurrences_in_array/

Section
 - Arrays

score
 - 100%
"""


from collections import Counter


def solution(A):
    c = Counter(A)
    for key, val in c.items():
        if val % 2 != 0:
            return key
