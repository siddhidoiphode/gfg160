
def prime(num,i=2):
    
    if i > num//2:
        return "Prime"
    if num % i==0 and i <= num//2:
        return "Not prime number"
    return prime(num,i+1)

num= 975
print(f"{num} is ",prime(num))