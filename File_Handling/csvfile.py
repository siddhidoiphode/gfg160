# import csv 
# r = csv.DictReader('C:/Users/Siddhi Doiphode/Downloads/test.csv')
# r.reader()
# print(r)

import csv

# Open the file properly
with open('C:/Users/Siddhi Doiphode/Downloads/test.csv', mode='r', newline='') as file:
    r = csv.DictReader(file)  # Pass the file object, not the file path string
    # print(r)
    # Iterate over the rows and print each one as a dictionary
    for row in r:
        print(row)

with open('C:/Users/Siddhi Doiphode/Downloads/test.csv', mode='a', newline='') as file:
    file.write(" "+'ABBCDEFGH')

