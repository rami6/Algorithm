"""
Problem description
 - https://app.codility.com/programmers/lessons/5-prefix_sums/genomic_range_query/

Section
 - Prefix Sums

score
 - 100%
"""


def solution(S, P, Q):
    d = {'A': 1, 'C': 2, 'G': 3, 'T': 4}

    minarr = []
    minimum = 4

    for i in range(len(P)):
        for key in d.keys():
            if S.find(key, P[i], Q[i] + 1) >= 0:
                minimum = min(minimum, d[key])
                if minimum == 1:
                    break
        minarr.append(minimum)
        minimum = 4

    return minarr
