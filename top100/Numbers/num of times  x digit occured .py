from collections import Counter

a = '12353245643245321221'
b = Counter(a).most_common(2)
print(b)
