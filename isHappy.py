def isHappy(num):
    """
        :type n: int
        :rtype: bool
        """
    n = 0
    one = 0
    c = 0
    nums = list(str(num))
    happy = False
    while not happy:
            c += 1
            for x in range(len(nums)):
                n += int(nums[x])**2
            nums = list(str(n))
            n = 0
            for y in range(len(nums)):
                one += int(nums[y])
            if one == 1:
                happy = True
            elif c > (5):
                happy = False
                break
            else:
                one = 0
    return happy
