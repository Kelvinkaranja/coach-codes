def thirdMax(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s=list(set(nums))
        s.sort()
        if len(s)>2:
            return s[-3]
        else:
            return max(s)
