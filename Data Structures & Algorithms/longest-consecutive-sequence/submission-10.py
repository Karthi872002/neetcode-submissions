class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()

        frequency = dict()
        for num in nums:
            frequency[num] = frequency.get(num,0) + 1
        
        nums = list(frequency.keys())
        window = []
        window.append(nums[0])
        length = len(nums)
        i = 1
        maximum = 1
        while i < length:
            if nums[i] - nums[i-1] == 1:
                window.append(nums[i])
               
                maximum = max(maximum,len(window))
               
            else:
    
                window = [nums[i]]
            i+=1
        
        
        return maximum
            