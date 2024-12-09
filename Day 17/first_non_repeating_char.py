# https://www.geeksforgeeks.org/batch/gfg-160-problems/track/string-gfg-160/problem/non-repeating-character-1587115620

class Solution:

    def nonRepeatingChar(self,s):
        letters = {}

        for char in s:
            if char not in letters:
                letters[char] = 1
            else:
                letters[char] += 1

        not_repeat = 1
        non_repeating_char = '$'

        for key, value in letters.items():
            if value == not_repeat:
                non_repeating_char = key
                break
        
        return non_repeating_char