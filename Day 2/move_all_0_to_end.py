# https://www.geeksforgeeks.org/batch/gfg-160-problems/track/arrays-gfg-160/problem/move-all-zeroes-to-end-of-array0751

# User function Template for python3

class Solution:
    def pushZerosToEnd(self, arr):
        # code here
        size = len(arr)
        i = 0
        count = 0

        while i < size:
            if arr[i] != 0:
                arr[count], arr[i] = arr[i], arr[count]
                count += 1
            i += 1

        return arr

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.pushZerosToEnd(arr)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1
