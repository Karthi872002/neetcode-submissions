class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_frequency = dict()
        t_frequency = dict()

    

        if len(s) != len(t):
            return False

        for char in s:
            s_frequency[char] = s_frequency.get(char,0)+1
        
        for char in t:
            t_frequency[char] = t_frequency.get(char,0)+1

        for i in s_frequency:
            if (i not in t_frequency) or  (s_frequency.get(i) != t_frequency.get(i)):
                
                return False
        return True  