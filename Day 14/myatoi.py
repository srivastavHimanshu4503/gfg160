# https://www.geeksforgeeks.org/batch/gfg-160-problems/track/string-gfg-160/problem/implement-atoi

class Solution:

    def myAtoi(self, s):

        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        n = len(s)
        i = 0

        sign = 1
        result = 0

        while i < n and s[i] == ' ':
            i += 1

        if i < n and (s[i] == '+' or s[i] == '-'):
            sign = -1 if s[i] == '-' else 1
            i += 1

        while i < n and s[i].isdigit():
            digit = int(s[i])

            if result > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN
            
            result = result*10 + digit

            i += 1

        return sign*result