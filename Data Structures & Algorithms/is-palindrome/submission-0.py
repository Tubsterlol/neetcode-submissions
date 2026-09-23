class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ""

        for c in s:
            if c.isalnum() == True:
                newStr += c.lower()
            else:
                pass
            
        if newStr == newStr[::-1]:
            return True
        else:
            return False