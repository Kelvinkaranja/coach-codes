# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        x=0
        while guess(x)!=0:
            if (n+x)%2!=0:
                x=(n+1)/2
                if guess(x)==-1:
                    for e in range(x):
                        if guess(e)==0:
                            x=e
                elif guess(x)==1:
                    for e in range(x,n+1):
                        if guess(e)==0:
                            x=e
                else:
                    return x
            else:
                x=n/2
                if guess(x)==-1:
                    for e in range(x):
                        if guess(e)==0:
                            x=e
                elif guess(x)==1:
                    for e in range(x,n+1):
                        if guess(e)==0:
                            x=e
                else:
                    return x
        return x
