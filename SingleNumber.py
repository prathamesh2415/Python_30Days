class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        for i in nums:
            val = nums[i]
            print("Value is ",val)            
            Diff = val ^ nums[i]    
            print("Difference :",Diff)
        return nums[i]    

s1 = Solution()
print(s1.singleNumber([2,2,1]))