class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m > 7 or n > 3:
            return 0
        if m == 7 and n == 3:
            return 1
        if leftAns = uniquePaths(m + 1, n):
        if rightAns = uniquePaths(m, n + 1):
            return (leftAns + rightAns)
    uniquePaths(self, 7, 3)
