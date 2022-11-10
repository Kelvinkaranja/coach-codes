def smallest_missing_int(nums):
    #SORT THE LIST
    nums.sort()
    #SET A START POINT
    count=1
    if count in nums:
        nums=list(set(nums[nums.index(count):]))
        nums.sort()
        for x in range(len(nums)):
            if nums[x]!=count:
                return count
            else:
                count += 1
    else:
        return count
    return count
        
