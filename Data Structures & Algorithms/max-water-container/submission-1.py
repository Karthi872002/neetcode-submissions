class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        maximum_volume = 0
        while i < j:
            min_heights = min(heights[i],heights[j])
            current_volume = (j-i) * min_heights
            maximum_volume = max(current_volume,maximum_volume)
            if heights[i] < heights[j] :
                i +=1
            else:
                j-=1
        
        return maximum_volume
            
        