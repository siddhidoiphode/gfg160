

class Solution:
    def dayOfYear(self, date: str) -> int:
        leap = False
        date=date.split('-')
        year=int(date[0])
        month=int(date[1])
        day=int(date[2])
        
        leap = (year%4==0 and year%100!=0 ) or (year%400 ==0)
       
        month_days=[0,31,28,31,30,31,30,31,31,30,31,30,31]

      
        m = sum( month_days[i]  for i in range(month) )
        print(m)
        days=day+m
        if leap == True and month >2:
            days += 1
            

        return days







# Code
# Testcase
# Test Result
# Test Result
# 1154. Day of the Year
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# Given a string date representing a Gregorian calendar date formatted as YYYY-MM-DD, return the day number of the year.

 

# Example 1:

# Input: date = "2019-01-09"
# Output: 9
# Explanation: Given date is the 9th day of the year in 2019.
# Example 2:

# Input: date = "2019-02-10"
# Output: 41
 