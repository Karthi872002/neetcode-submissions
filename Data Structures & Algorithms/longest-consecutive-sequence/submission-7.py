class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        frequencies = {}

        if not nums:
            return 0

        for num in nums:
            frequencies[num] = frequencies.get(num, 0) + 1

        distinct = sorted(frequencies.keys())

        window = [distinct[0]]
        max_length = 1

        right = 1

        while right < len(distinct):
            if distinct[right] - distinct[right - 1] == 1:
                window.append(distinct[right])
            else:
                window = [distinct[right]]

            max_length = max(max_length, len(window))
            right += 1

        return max_length