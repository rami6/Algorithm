"""
Problem description
 - https://app.codility.com/programmers/lessons/1-iterations/binary_gap/

Section
 - Iterations

score
 - 100%
"""


def solution(N):
    bin_N = bin(N)
    str_bin_N = str(bin_N)[2:]

    zero_max = 0
    one_inds = []

    i = 0
    while i < len(str_bin_N):
        ind = str_bin_N.find('1', i)
        if ind >= 0:
            one_inds.append(ind)
            i = ind + 1
        else:
            break

    for i in range(1, len(one_inds)):
        zeros = one_inds[i] - one_inds[i - 1] - 1
        zero_max = max(zero_max, zeros)

    return zero_max