# https://www.geeksforgeeks.org/batch/gfg-160-problems/track/arrays-gfg-160/problem/smallest-positive-missing-number-1587115621

#User function Template for python3

class Solution:
    
    #Function to find the smallest positive number missing from the array.
    def missingNumber(self,arr):
        #Your code here
        # TC = O(nlogn) and SC = O(1)
        # arr.sort()
        # smallest_number = 1
        # for num in arr:
        #     if num == smallest_number:
        #         smallest_number += 1
        #     elif num > smallest_number:
        #         break
        # return smallest_number
        
        # Visited Array 
        # TC = O(n) and SC = O(n)
        # n = len(arr)
        # temp = [False]*n
        # for i in range(n):
        #     if 1 <= arr[i] <= n:
        #         temp[arr[i]-1] = True

        # for i in range(n):
        #     if not temp[i]:
        #         return i+1

        # return n+1
        
        # Cycle sort
        # TC = O(n) and SC = O(1)
        n = len(arr)
        for i in range(n):
            while 1 <= arr[i] <= n and arr[i] != arr[arr[i]-1]:
                temp = arr[i]
                arr[i] = arr[temp - 1]
                arr[temp - 1] = temp
                
        for i in range(n):
            if i != arr[i]-1:
                return i+1
                
        return n+1