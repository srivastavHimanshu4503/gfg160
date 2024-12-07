# https://www.geeksforgeeks.org/batch/gfg-160-problems/track/arrays-gfg-160/problem/maximum-product-subarray3604

#User function Template for python3
class Solution:

    # Function to find maximum
    # product subarray
    def maxProduct(self,arr):
        # code here
#         cmx = cmn = res = arr[0]
        
#         for i in range(1, len(arr)):
#             temp = max(arr[i], arr[i]*cmx, arr[i]*cmn)
            
#             cmn = min(arr[i], arr[i]*cmx, arr[i]*cmn)
            
#             cmx = temp
            
#             res = max(res, cmx)
            
#         return res

        n = len(arr)
        i = 0
        j = n-1
        lr = rl = 1
        res = float('-inf')
        while i < n:
            if lr == 0:
                lr = 1
            if rl == 0:
                rl = 1
            lr = lr*arr[i]
            rl = rl*arr[j]
            res = max(res, lr, rl)
            i += 1
            j -= 1
        return res
