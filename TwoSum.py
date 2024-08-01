class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        valCheck = {}
        for i in range(len(nums)):
            
            if nums[i] in valCheck.keys():
                print(valCheck.keys())
                return [valCheck[nums[i]],i]
            
            remaining = target - nums[i]
            valCheck[remaining] = i                 
           
s1 = Solution()
print(s1.twoSum([3,2,3],6))