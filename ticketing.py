
def timeRequiredToBuy(self, tickets, k):
        """
        :type tickets: List[int]
        :type k: int
        :rtype: int
        """
        time=0
        while tickets[k]>0:
            for i in range(len(tickets)):
                if tickets[k]==0:
                    return time
                if tickets[i]>0:
                    tickets[i]=tickets[i]-1
                    time +=1
        
        
        
