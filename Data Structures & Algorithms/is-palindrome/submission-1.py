

class Solution:
    def isPalindrome(self, s: str) -> bool:
        news= ""
        for x in s:
            if (ord(x)<=ord('z') and ord(x)>=ord('a')) or (ord(x)<=ord('Z') and ord(x)>=ord('A')) or  (ord(x)<=ord('9') and ord(x)>=ord('0')):
                news+=x
            


        if news.lower() == news[::-1].lower():
            return True
        return False