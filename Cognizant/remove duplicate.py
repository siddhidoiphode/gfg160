# Only keep first occurrence of each element in a list


s = "   programming ".strip()
ans = ''.join(dict.fromkeys(s))
print(ans)




# old=[]
# s="   programming ".strip()
# ans=""
# for i in s:
#     if i not in old:
#         ans+=i
#         old.append(i)

# print(ans)