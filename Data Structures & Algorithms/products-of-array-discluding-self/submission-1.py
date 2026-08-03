class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
    
        products = [1]*len(nums)
        
        for i in range(len(nums)):
            
            for j in range(len(nums)):
                if i != j:
                    products[j] *= nums[i]
        
        return products