"""
Problem description
 - https://app.codility.com/programmers/lessons/5-prefix_sums/min_avg_two_slice/

Section
 - Prefix Sums

score
 - 80%
"""


def solution(A):
    min_ave = (A[-2] + A[-1]) / 2
    min_ind = len(A) - 2
    count = 2

    i = len(A) - 3
    while i >= 0:
        # Check if the slice with minimum average can be extended.
        if i == min_ind - 1:
            if A[i] <= min_ave:
                min_ave = (min_ave * count + A[i]) / (count + 1)
                count += 1
                min_ind = i

        # Check which is smaller current min_ave or average of (A[i] + A[i + 1])
        if (A[i] + A[i + 1]) / 2 <= min_ave:
            min_ave = (A[i] + A[i + 1]) / 2
            count = 2
            min_ind = i

        i -= 1

    return min_ind