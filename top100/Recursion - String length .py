
i=0
def lenString(s):
    global i
    try:
        if s[i]:
            i+=1
    except IndexError:
        return i
    return lenString(s)


s='siddhunkk'
print("Length of string is ",lenString(s))

