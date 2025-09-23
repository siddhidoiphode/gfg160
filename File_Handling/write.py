
# Write mode
with open('temp.py', mode='w') as t:
    t.write("write123")

# Read mode
with open('temp.py', mode='r') as t:
    data = t.read()

print("Read from file:", data)

# Append mode
with open('temp.py', mode='a') as t:
    text = input("enter txyt to write in file temp: ")
    t.write(" "+text)

# Read again to see the updated content
with open('temp.py', mode='r') as t:
    updated_data = t.read()

print("After appending:", updated_data)

