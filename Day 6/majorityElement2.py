# https://geeksforgeeks.org/batch/gfg-160-problems/track/arrays-gfg-160/problem/majority-vote


class Solution:
    
    #Function to find the first non-repeating character in a string.
    def nonRepeatingChar(self,s):
        #code here
        letters = {}
        for char in s:
            if char not in letters:
                letters[char] = 1
            else:
                letters[char] += 1
    
        not_repeat = 1
        not_repeated_char = '$'
        for key, value in letters.items():
            if value == not_repeat:
                not_repeated_char = key
                break
    
        return not_repeated_char
