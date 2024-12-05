# https://www.geeksforgeeks.org/batch/gfg-160-problems/track/arrays-gfg-160/problem/kadanes-algorithm-1587115620

class Solution:
    def maxSubArraySum(self,arr):
        res = maxEnd = arr[0]

        for i in range(1, len(arr)):
            maxEnd = max(maxEnd + arr[i], arr[i])

            res = max(res, maxEnd)

        return res