# https://www.geeksforgeeks.org/batch/gfg-160-problems/track/string-gfg-160/problem/anagram-1587115620

#User function Template for python3

class Solution:
    
    #Function is to check whether two strings are anagram of each other or not.
    def areAnagrams(self, s1, s2):
        
        MAX_CHAR = 26
        if len(s1) != len(s2):
            return False
            
        # Method 1: TC: O(m*log(m) + nlog(n))
        # SC: O(1) where strings are mutable  

        # return sorted(s1) == sorted(s2)
        
        # Method 2: Using Heap or Dictionary
        # characters = {}
        
        # for char in s1:
        #     if char not in characters:
        #         characters[char] = 1
        #     else:
        #         characters[char] += 1
                
        # for char in s2:
        #     if char in characters:
        #         characters[char] -= 1
                
        # for val in characters.values():
        #     if val != 0:
        #         return False
                
        # return True
        
        # Method 3: Using Frequency Array\
        freq = [0] * MAX_CHAR
    
        # Count frequency of each character in string s1
        for ch in s1:
            freq[ord(ch) - ord('a')] += 1
    
        # Count frequency of each character in string s2
        for ch in s2:
            freq[ord(ch) - ord('a')] -= 1
    
        # Check if all frequencies are zero
        for count in freq:
            if count != 0:
                return False
                
        return True