
class Movie:
    def __init__(self , name, hero ):
        self.name = name
        self.hero = hero

    def display(self):
        print(f'Name of movie is {self.name}, hero is {self.hero}')

movie_names = []
while True :
    name = input("Movie name: ")
    hero = input("Enter hero of Movie: ")
    obj = Movie(name,hero)

    movie_names.append(obj)
    ans = input("Do u want to add another movie? (y/n)")

    if ans != 'y' :
        break
print("___________________________________________________________________________________")
for obj in movie_names:
    obj.display()
