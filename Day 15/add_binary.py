# https://www.geeksforgeeks.org/batch/gfg-160-problems/track/string-gfg-160/problem/add-binary-strings3805

class Solution:

    def addBinary(self, s1: str, s2: str) -> str:
        # Assure that s1 is the bigger one
        if len(s1) < len(s2):
            s1, s2 = s2, s1

        s2 = s2.zfill(len(s1))

        carry = 0
        res = []

        for i in range(len(s1)-1, -1, -1):
            bit1 = int(s1[i])
            bit2 = int(s2[i])

            total = bit1 + bit2 + carry

            res.append(str(total%2))
            carry = total//2

        if carry:
            res.append('1')

        ans = ''.join(res)[::-1]

        i = 0
        while i < len(ans) and ans[i] == '0':
            i += 1

        return ans[i:]