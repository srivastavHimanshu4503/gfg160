class Solution:
    def lps(self, pat):
        m = len(pat)
        lps = [0]*m
        i = 1
        length = 0
        while i < m:
            if pat[i] == pat[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length-1]
                else:
                    lps[i] = 0
                    i += 1
        return lps
    
    def search(self, txt, pat):
        n = len(txt)
        m = len(pat)

        lps = self.lps(pat)
        indices = []

        i = 0
        j = 0
        while i < n:
            if txt[i] == pat[j]:
                i += 1
                j += 1
            if j == m:
                indices.append(i-j)
                j = lps[j-1]
            elif i < n and txt[i] != pat[j]:
                if j != 0:
                    j = lps[j-1]
                else:
                    i += 1
        
        return indices

if __name__ == "__main__":
    t = int(input("Enter number of test cases: "))

    while t:
        obj = Solution()
        print(obj.search(txt := input("Enter text: "), pat := input("Enter pattern: ")))
        t -= 1
    