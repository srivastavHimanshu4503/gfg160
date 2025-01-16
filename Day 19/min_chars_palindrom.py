class Solution:
    def build_lps(self, pat):
        m = len(pat)
        lps = [0]*m

        i = 1
        len_ = 0

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

        return lps
    
    def minChar(self, s):
        text = s + '#' + s[::-1]
        lps = self.build_lps(text)
        return len(s) - lps[-1]

if __name__ == '__main__':
    test_case = int(input("Enter number of test cases: "))

    while test_case:
        obj = Solution()
        print(obj.minChar(s := input("Enter word :")))
        test_case -= 1