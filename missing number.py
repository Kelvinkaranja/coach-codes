def missingNumber(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #Declare Variables and sort your list
        n=len(nums)
        nums.sort()
        #iterate through list
        for e in range(n+1):
                #add number at the end of list if still not found
            if e==n and len(nums)==n:
                x=n
                nums.append(x)
                #find missing number
            else:
                if nums[e]!=e:
                    x=e
                    nums.append(x)
                    nums.sort()
        return x
