 
n='43521'
li1=list(n)
li=[n[i:i+2] for i in range(len(n)) if i+1 < len(n) and int(n[i:i+2]) <27 ]
li+=li1
print(li)

