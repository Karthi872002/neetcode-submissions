class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        frequency = {}
        if s == "":
            return 0
        length = len(s) - 1
        left = 0
        right = 1
        frequency[s[left]] = frequency.get(s[left],0) +1
        maximum = 1
        while right <= length:
            frequency[s[right]] = frequency.get(s[right],0) +1
            while frequency[s[right]] > 1:
                frequency[s[left]] -= 1
                if frequency[s[left]] == 0:
                    del frequency[s[left]]
                left += 1
          
            maximum = max(len(frequency),maximum)
            right+=1
        print(frequency)
        return maximum