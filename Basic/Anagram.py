
class Anagram:
    def isAnagram(self,str1,str2):
        self.str1 = str1.lower()
        self.str2 = str2.lower()

        if sorted(self.str1) == sorted(self.str2):
            print("Anagram")
        else:
            print("Not Anagram")

str1=input("Enter first string: ").strip()
str2=input("Enter second string: ").strip()
obj1=Anagram()
obj1.isAnagram(str1, str2)

