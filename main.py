def calc1(n):
    return n*(n+1)/2
print(calc1(7))

def calc2(n):
    sum = 0
    for i in range(1,n+1):
        sum+=i
    return sum
#print(calc2(7))

def calc3(n):
    sum = 0
    for i in range (1,n+1):
        for i in range(1,i+1):
            sum+=1
    return sum

#print(calc3(7))