class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        sum = 0
        a = {"I":1,"V":5, "X":10, "L":50,"C":100,"D":500,"M":1000}
        i=0
        while i<len(s):
            #print(">>>",i,"   ",sum)
            cha=s[i]
            if i == len(s)-1:
                sum += a[cha]
                i+=1
                continue
            if cha == "C" and (s[i+1] == "D" or s[i+1] =="M"):
                sum += a[s[i+1]] - a[cha]
                #print("I'm here! Ready to jump")
                i += 1
            elif cha == "X" and (s[i+1] == "L" or s[i+1] =="C"):
                sum += a[s[i+1]] - a[cha]
                i += 1
            elif cha == "I" and (s[i+1] == "V" or s[i+1] =="X"):
                sum += a[s[i+1]] - a[cha]
                i += 1
            else:
                sum += a[cha]
                
            i+=1
        return sum