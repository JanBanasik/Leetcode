class Solution(object):
    def minOperations(self, s):
        """
        :type s: str
        :rtype: int
        """
        counter1 = 0 # 101010....
        counter2 = 0 # 010101....
        for i in range(len(s)):
            if i % 2 == 0:
                counter1 += (1 if s[i] == '0' else 0)
                counter2 += (1 if s[i] == '1' else 0)
            else:
                counter2 += (1 if s[i] == '0' else 0)
                counter1 += (1 if s[i] == '1' else 0)
        return min(counter1,counter2)