# class Solution:
#     def climbStairs(self, n: int) -> int:
        
#         if n<=2 :
#             return n
#         f,l=1,2
#         for i in range(3,n+1):
#             f,l=l,f+l
#         return l

n=5  
if n<=2:
    print(n)
f=1
l=2
for i in range(n-2):
    next=f+l
    f=l
    l=next

print(l)


# 0
# 0Streaks
# Practice Time!
# DCC Badge

# avatar
# Avatar
# SiddhiDoiphode
# Access all features with our Premium subscription!
# myLists
# My Lists
# notebook
# Notebook
# submissions
# Submissions
# progress
# Progress
# points
# Points
# Try New Features
# Orders
# My Playgrounds
# Settings
# Appearance
# Sign Out
# Premium
# Description
# Editorial
# Editorial
# Solutions
# Solutions
# Submissions
# Submissions
# Code
# Testcase
# Test Result
# Test Result
# 70. Climbing Stairs
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

# Example 1:

# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# Example 2:

# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step