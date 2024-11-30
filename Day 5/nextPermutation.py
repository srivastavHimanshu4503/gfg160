def lexicographical_order(arr):
    for i in range(len(arr)):
        swapping = False
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapping = True
        if not swapping:
            return arr
    return arr

    
class Solution:
    def nextPermutation(self, arr):
        pivotIndex = -1

        for i in range(len(arr)-2, -1, -1):
            if arr[i]  < arr[i+1]:
                pivotIndex = i
                break

        if pivotIndex == -1:
            arr.sort()
            return arr

        for i in range(len(arr)-1, -1, -1):
            # Perform swapping
            if arr[i] > arr[pivotIndex]:
                arr[pivotIndex], arr[i] = arr[i], arr[pivotIndex]
                break
        
        arr[pivotIndex+1: ] = lexicographical_order(arr[pivotIndex+1:])
    
        return arr


test = Solution()

print(test.nextPermutation([2, 4, 1, 7, 5, 0])) # Output: [2, 4, 5, 0, 1, 7]
print(test.nextPermutation([1, 2, 3, 6, 5, 4])) # Output: [1, 2, 4, 3, 5, 6]