def revmul(nums):
    
    a=len(nums)
    ans=[]
    x=-1
    total=1
    #clone the array for comparison
    we=[]
    for e in nums:
        we.append(e)
    #check for zeros and remove them
    for e in we:
        if e==0:
            we.pop(we.index(e))
    #check for multiple zeros
    b=len(we)
    if a-b>1:
        while a>0:
            ans.append(0)
            a=a-1
    elif a-b<=1:
    #find the total multiple if 1 or no zeros are found
        while b>0 :
            total=total*we[x+1]
            b=b-1
            x=x+1
        b=len(we)
        if a-b==1:
            while a>0:
                ans.append(0)
                a=a-1
            for each in nums:
                    if each==0:
                        ans[nums.index(0)]=total
        #account for non-zero list
        else:
            for each in nums:
                answer=int(total/each)
                ans.append(answer)
    return ans
revmul([1,5,8,3,7])

