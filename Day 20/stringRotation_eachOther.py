class Solution:
    def build_lps(self, pat):
        # Initializing variables
        m = len(pat)
        lps = [0]*m
        i = 1
        len_ = 0

        # Iterating over pattern to make lps array
        while i < m:
            if pat[i] == pat[len_]:
                len_ += 1
                lps[i] = len_
                i += 1
            else:
                if len_ != 0:
                    len_ = lps[len_-1]
                else:
                    lps[i] = 0
                    i += 1

        # Returning the lps array
        return lps
    
    def areRotations(self, s1, s2):
        if len(s1) != len(s2):
            return False
        
        # Method 1:
        # return s2 in (s1+s1)

        # Method 2:
        txt = s1 + s1
        lps = self.build_lps(s2)
        i = j = 0
        while i < len(txt):
            if txt[i] == s2[j]:
                i += 1
                j += 1
                if j == len(s2):
                    return True
            else:
                if j != 0:
                    j = lps[j-1]
                else:
                    i += 1
        return False
    
if __name__ == '__main__':
    t = int(input("Enter number of test cases you want to perform: "))
    while t:
        obj = Solution()
        print(obj.areRotations(s1 := input("Enter s1: "), s2 := input("Enter s2: ")))
        t -= 1
