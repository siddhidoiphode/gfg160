def lengthOfLongestSubstring(s):
    seen = set()  # to keep track of characters in the current substring
    max_len = 0   # stores the maximum length found
    start = 0     # the starting index of the current substring
    
    for end in range(len(s)):  # 'end' goes from start to end of the string
        while s[end] in seen:  # if current char is already in the substring
            seen.remove(s[start])  # remove the first char and move 'start' forward
            start += 1
        seen.add(s[end])  # add current char to the substring
        max_len = max(max_len, end - start + 1)  # update max length
    
    return max_len




# 3. Longest Substring Without Repeating Characters
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# Given a string s, find the length of the longest substring without duplicate characters.

 

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.