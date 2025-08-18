
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits=int( "".join(map(str,digits)) )
        digits+=1
        # print(digits)
        digits = [int(i) for i in str(digits)]
        # print(digits)
        return digits
