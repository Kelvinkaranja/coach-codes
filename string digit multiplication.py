def multiply(num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        #Declare variables
        n=len(num1)
        nums1=[]
        #Iterate through list 1
        for e in range(n):
            loop=True
            x=0
            #Create loop to change string to digit without using int operator
            while loop:
                if num1[e]==str(x):
                    nums1.append(x)
                    loop=False
                else:
                    x +=1
        #Iterate through list 2
        numb1=0
        for e in range(n):
            numb1 += nums1[e]*(10**(n-e-1))
        n2=len(num2)
        nums1=[]
        for e in range(n2):
            loop=True
            x=0
            #Create loop to change string to digit without using int operator
            while loop:
                if num2[e]==str(x):
                    nums1.append(x)
                    loop=False
                else:
                    x +=1
        numb2=0
        #Multiply elements in the list with its factor
        for e in range(n2):
            numb2 += nums1[e]*(10**(n2-e-1))
        return str(numb1*numb2)
