class Solution:
    def canAliceWin(self,nums:list[int]):
        sum=0
        TwoDigit = 0
        for i in nums:
            if 0 <= i <= 9:
                sum =sum+i
            elif 10 <= i <= 99:
                TwoDigit = i
        if(sum != TwoDigit):
            return True
        else:
            return False
        
        
S1 = Solution()
print(S1.canAliceWin([5,5,5,25]))