#Make necessary importance
import math
#Define your fuction
def isPowerOfTwo(n):
        """
        :type n: int
        :rtype: bool
        """
        if n<=0:
            return False
        else:
            ans=math.log(n,(2))
            fl=round(ans,10)
            return (fl)-int(float(ans))==0
