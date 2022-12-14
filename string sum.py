def addStrings(self, num1, num2):
    """
        :type num1: str
        :type num2: str
        :rtype: str
    """
    nums1 = []
    nums2 = []
    d1 = 0
    d2 = 0
    for i in range(10):
        for e in range(len(num1)):
            if num1[e] == str(i):
                    nums1.append(i)
        for e in range(len(num2)):
            if num2[e] == str(i):
                    nums2.append(i)
    l1 = len(nums1)
    l2 = len(nums2)
    for i in range(l1):
        d1 += nums1[i]*(10**(l1-1))
        l1 -= 1
    for i in range(l2):
        d2 += nums2[i]*(10**(l2-1))
        l2 -= 1
    return str(d1+d2)
