# https://www.geeksforgeeks.org/batch/gfg-160-problems/track/arrays-gfg-160/problem/max-circular-subarray-sum-1587115620

def circularSubarraySum(arr):
    ##Your code here
    max_subarray_sum = arr[0]
    min_subarray_sum = arr[0]
    current_max_sum = 0
    current_min_sum = 0
    total_sum = 0
    
    for i in range(len(arr)):
        
        # For calculating maximum subarray sum
        current_max_sum = max(current_max_sum+arr[i], arr[i])
        max_subarray_sum = max(current_max_sum, max_subarray_sum)
        
        
        current_min_sum = min(current_min_sum+arr[i], arr[i])
        min_subarray_sum = min(current_min_sum, min_subarray_sum)
        
        total_sum += arr[i]

    max_circular_sum = total_sum - min_subarray_sum
    
    if min_subarray_sum == total_sum:
        return max_subarray_sum
        
    return max(max_circular_sum, max_subarray_sum)