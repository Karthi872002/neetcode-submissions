class Solution:
    def isPalindrome(self, s: str) -> bool:

        left = 0
        length = len(s) -1 
        right = len(s) -1
        while left < right and left < length  :
            while left < right and not s[left].isalnum():
                left +=1
            while left < right and not s[right].isalnum():
                right -=1
            
            if s[left].lower() != s[right].lower():
                return False
            print(s[left])
            print(s[right])
            left +=1
            right -=1
        
        return True
        
        