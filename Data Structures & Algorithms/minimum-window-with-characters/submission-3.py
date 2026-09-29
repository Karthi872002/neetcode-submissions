class Solution:
    def minWindow(self, s: str, t: str) -> str:

        lookup = dict()
        for i in range(len(t)):
            lookup[t[i]] = lookup.get(t[i],0)+1
        
        left = 0
        right = 0
        window = {}
        minimum = ""
        length = len(s)
        need = len(lookup)
        having = 0

        while right < length:

            char = s[right]
           
            window[char] = window.get(char,0) + 1
            if char in lookup and window[char] == lookup[char]:
                having +=1
                print(char)
                print(having)

            
            while having == need:
                
                current = s[left:right+1]
        
                if minimum == "" or len(current) < len(minimum):
                    minimum = current
                
                left_char = s[left]
                window[left_char] -= 1

                if left_char in lookup and window[left_char] < lookup[left_char]:
                    having -=1
                left +=1
            
            right+=1
        return minimum
              
    
