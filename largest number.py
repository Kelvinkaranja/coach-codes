'''
Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.

Since the result may be very large, so you need to return a string instead of an integer.
'''


def largestNumber(nums):
    """
        :type nums: List[int]
        :rtype: str
        """
    top = len(str((max(nums))))
    new = []
    stransw = ''
    for e in range(len(nums)):
        if len(str(nums[e])) < top:
            new.append(nums[e]*10**(top-len(str(nums[e]))))
        else:
            new.append(nums[e])
    new.sort()
    new.reverse()
    for x in range(len(new)):
        if new[x] in nums:
            stransw += str(new[x])
            nums.pop(nums.index(new[x]))
        else:
            while new[x] not in nums:
                new[x] = int(new[x]/10)
            stransw += str(new[x])
            nums.pop(nums.index(new[x]))
    return stransw
