import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_product = []
        product = 1
        for i in range(len(nums)):
            left_product.append(product)
            product = product * nums[i]
        
        right_product = []
        pos = len(nums)-1
        product = 1
        while pos >= 0:
            right_product.append(product)
            product *= nums[pos]
            pos -=1

        right_product.reverse()
        
        
        result = []
        for i in range(len(left_product)):
            product = left_product[i] * right_product[i]
            result.append(product)
        return result


            
            

        

      
            