#Make necessary importance
import math
#Define your fuction
def isPowerOfTwo(n):
        """
        :type n: int
        :rtype: bool
        """
        #Isolate cases of 0
        if n<=0:
            return False
        #Account for all other cases
        else:
            ans=math.log(n,(2))
            fl=round(ans,10)
            #Make a comparison to assert equality
            return (fl)=int(float(ans))
