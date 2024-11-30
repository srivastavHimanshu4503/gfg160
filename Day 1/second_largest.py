# https://www.geeksforgeeks.org/batch/gfg-160-problems/track/arrays-gfg-160/problem/second-largest3735
# 27th Nov 2024

class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        largest = second_largest = float('-inf')
        for num in arr:
            if num > largest:
                second_largest = largest
                largest = num
            elif (num > second_largest) and (num != largest):
                second_largest = num
                
        return -1 if second_largest == float('-inf') else second_largest

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.getSecondLargest(arr)
        print(ans)
        print("~")