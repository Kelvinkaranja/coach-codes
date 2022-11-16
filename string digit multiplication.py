def multiply(num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        n=len(num1)
        nums1=[]
        for e in range(n):
            loop=True
            x=0
            while loop:
                if num1[e]==str(x):
                    nums1.append(x)
                    loop=False
                else:
                    x +=1
        numb1=0
        for e in range(n):
            numb1 += nums1[e]*(10**(n-e-1))
        n2=len(num2)
        nums1=[]
        for e in range(n2):
            loop=True
            x=0
            while loop:
                if num2[e]==str(x):
                    nums1.append(x)
                    loop=False
                else:
                    x +=1
        numb2=0
        for e in range(n2):
            numb2 += nums1[e]*(10**(n2-e-1))
        return str(numb1*numb2)
