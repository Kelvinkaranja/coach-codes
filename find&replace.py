def findErrorNums(nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        nums.sort()
        count=0
        #iterate to find repeating numbers
        for x in range(n):
            if nums.count(nums[x])>1:
                a=nums[x]
        #remove the number from the array
        nums.pop(nums.index(a))
        #check through the order and keep count of the missing number and find it
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
