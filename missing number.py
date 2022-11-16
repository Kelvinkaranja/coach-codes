def missingNumber(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        n=len(nums)
        nums.sort()
        for e in range(n+1):
            if e==n and len(nums)==n:
                x=n
                nums.append(x)
            else:
                if nums[e]!=e:
                    x=e
                    nums.append(x)
                    nums.sort()
        return x
