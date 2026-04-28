class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        l,r = 0,2
        length = 1
        if len(s) ==1:
            return s
        else:
            temp = s[0]
            while l<r and r<=len(s):
                #print(s[l:r], l, r)
                if len(temp)<(r-l+1) and self.isPalindrome(s[l:r]):
                    temp = s[l:r]
                    length = len(temp)
                r += 1
                if r>len(s):
                    l=l+1
                    r=l+len(temp)
            return temp
                

    def isPalindrome(self,s):
        return s==s[::-1]