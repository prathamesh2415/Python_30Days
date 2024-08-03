class Solution:
    def isPalindrome(self, x: int) -> bool:
        x =list[x]
        return x.reverse(x)
        #print(type(x))
    

s1 = Solution()
print(s1.isPalindrome(121))