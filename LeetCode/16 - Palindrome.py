
class Palindrome:
    def __init__(self,word):
        self.word = word.lower()
        self.rev = "".join(reversed(self.word))
        print(self.word)
        print(self.rev)
        
        if self.word == self.rev :
            print("Palindrome")
        else:
            print("Not Palindrome")
        
obj= Palindrome(",mkjbjl")

