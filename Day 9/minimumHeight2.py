# https://www.geeksforgeeks.org/batch/gfg-160-problems/track/arrays-gfg-160/problem/minimize-the-heights3351

class Solution:

    def getMinDiff(self, arr: list, k):
        n = len(arr)
        arr.sort()

        res = arr[n-1] - arr[0]

        for i in range(1, len(arr)):
            if arr[i]-k < 0:
                continue

            minH = min(arr[0]+k, arr[i]-k)
            maxH = max(arr[i-1]+k, arr[n-1]-k)

            res = min(res, maxH-minH)

        return res
    

if __name__ == "__main__":
    test = Solution()
    ans = test.getMinDiff([1, 2, 3, 5, 8, 10], 2)
    print(ans)