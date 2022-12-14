'''
Find 2 numbers in an array that ad up to a certain given target.
'''

def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n=len(nums)
        k=0
        while n>0:
            diff=target-nums[k]
            if diff in nums and nums.index(diff) != k:
                return [k,nums.index(diff)]
            else:
                k+=1
                n-=1
