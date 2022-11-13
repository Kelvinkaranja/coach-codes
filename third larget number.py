def thirdMax(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #Create unique list of nums and sort it
        s=list(set(nums))
        s.sort()
        #Find the third last digit in the list if it exists
        if len(s)>2:
            return s[-3]
        #Find the largest number if the third larget
        else:
            return max(s)
