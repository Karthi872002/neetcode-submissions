class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        left = 0
        right = 1
        length = len(prices)
        max_profit = 0
        if length == 2:
             max_profit  = max((prices[right] - prices[left]),max_profit)
             return max_profit
       
        while right < length-1 and left < right:
            print(left,right)
            if prices[right+1] > prices[right] :
                max_profit  = max((prices[right+1] - prices[left]),max_profit)
            else:
                
                max_profit  = max((prices[right] - prices[left]),max_profit)
                print(max_profit)
            if prices[right] < prices[left]:
                left = right
                print(left,right)
        
            right+=1

            if right == length-1 :
                 max_profit  = max((prices[right] - prices[left]),max_profit)
        return max_profit

            
            
        