class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        frequency = dict()
        for num in nums:
            if num in frequency:
                return True 
            else:
                frequency[num] = frequency.get(num,0) + 1
        return False
        
       
        