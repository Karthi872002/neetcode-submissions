class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = dict()
        for num in nums:
            frequency[num] = frequency.get(num,0) +1

        
        frequency = dict(sorted(frequency.items(),key = lambda x : x[1],reverse = True))

        num_keys = list(frequency.keys())
        return num_keys[0:k]
