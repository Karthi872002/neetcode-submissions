class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        length = len(nums)
        pairs = []

        for i in range(length - 2):

            left = i + 1
            right = length - 1

            while left < right:

                sumx = nums[i] + nums[left] + nums[right]

                if sumx == 0:
                    pairs.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                elif sumx < 0:
                    left += 1

                else:
                    right -= 1

        frequency = {}

        for arr in pairs:
            arr.sort()

        for pair in pairs:
            frequency[tuple(pair)] = frequency.get(tuple(pair), 0) + 1

        return list(frequency.keys())