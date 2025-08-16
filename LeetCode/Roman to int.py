class Solution:
    def romanToInt(self, s: str) -> int:
        # s=[I ,V ,X ,L ,C ,D ,M]
        # v=[1 ,5 ,10 ,50 ,100 ,500 ,1000]
        # "LVIII"
        total=0
        d={'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        s=s.upper()
        for i in range(len(s)):
            # current=d[s[i]]
            # nextt=d[s[i+1]]
            if  i+1 <len(s)  and d[s[i]] < d[s[i+1]]:
                total -= d[s[i]]
            else:
                total += d[s[i]]
        
        return total

        
            

