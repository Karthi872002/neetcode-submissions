class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers)-1

        while i < j:
            
            sumx = numbers[i] + numbers[j]
            if sumx == target:
                return [i+1,j+1]

            elif sumx < target:
                i+=1
            
            else:
                j-=1
          
            
