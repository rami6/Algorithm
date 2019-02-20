"""
Problem description
 - https://leetcode.com/problems/k-closest-points-to-origin/

Result
 - Runtime: 360 ms, faster than 95.41% of Python online submissions for K Closest Points to Origin.
 - Memory Usage: 15.1 MB, less than 74.44% of Python online submissions for K Closest Points to Origin.
"""


class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """

        points.sort(key=lambda point: point[0] ** 2 + point[1] ** 2)
        return points[:K]
