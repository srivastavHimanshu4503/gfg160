# https://www.geeksforgeeks.org/batch/gfg-160-problems/track/arrays-gfg-160/problem/rotate-array-by-n-elements-1587115621
def gcd(num1, num2):
    while num2:
        num1, num2 = num2, num1%num2
    return num1

def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1        
    return arr

class Solution:
    #Function to rotate an array by d elements in counter-clockwise direction. 
    def rotateArr(self, arr, d):
        #Your code here
        n = len(arr)
        if d > n:
            d = d%n
        
        number_of_iterations = gcd(n, d)       
        
        for i in range(number_of_iterations):
            currentElement = arr[i]
            
            currentIndex = i
            
            while True:
                
                nextIndex = (currentIndex + d)%n
                
                if nextIndex == i:
                    break
                
                arr[currentIndex] = arr[nextIndex]
                currentIndex = nextIndex
                
            arr[currentIndex] = currentElement
            
        return arr
    
    def rotateArr2(self, arr, d):
        #Your code here
        n = len(arr)
        if d > n:
            d = d%n
        
        arr = reverse(arr, 0, d-1)

        arr = reverse(arr, d, n-1)

        arr = reverse(arr, 0, n-1)
            
        return arr
    

obj1 = Solution()
print(obj1.rotateArr([1, 2, 3, 4, 5], 3))
print(obj1.rotateArr2([1, 2, 3, 4, 5], 3))