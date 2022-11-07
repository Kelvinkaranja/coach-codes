def findErrorNums(nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        nums.sort()
        count=0
        for x in range(n):
            if nums.count(nums[x])>1:
                a=nums[x]
        nums.pop(nums.index(a))
        for y in range(len(nums)):
            if nums[y]!=y+1 :
                b=y+1
                nums.append(b)
                nums.sort()
                count +=1
        if count==0:
            b=len(nums)+1
            nums.append(b)
        return [a,b]
