# 4.2 Remove duplicates from a string
# Problem: Remove duplicate characters from a string, keeping only the first occurrence.
# Example:
# Input: "programming" → Output: "progamin"

 
s=input("Enter a string: ").strip()
sl=list(s)
old=[]
new=""

for i in sl:
    if i not in old:
        new+=i
        old.append(i)
        
print("String after removing duplicates:", new)
