def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #Declare variables
        n=len(nums)
        k=0
        while n>0:
            diff=target-nums[k]
            if diff in nums:
                return [k,nums.index(diff)]
            else:
                k+=1
                n-=1
