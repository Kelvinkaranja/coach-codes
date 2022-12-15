def greatestLetter(self, s):
        """
        :type s: str
        :rtype: str
        """
        output=['']
        for i in range(len(s)):
            if s[i].isupper() and s[i].lower() in s:
                output.append(s[i])
        output.sort()
        return output[-1]
