class Solution:
    def arraySign(self, nums: List[int]) -> int:

        ans =1         #一開始的答案是正確的
        for n in nums: #依序取n出來
            ans *= n   #答案 乘n
        
        if ans>0:return 1       
        if ans<0:return -1
        if ans=0:return 0
