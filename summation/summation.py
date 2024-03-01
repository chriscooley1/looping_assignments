def summation_while(n:int) -> int:
    sum = 0
    i = 1
    while i <= n:
        sum += i
        i += 1
    return sum

def summation_for(n:int) -> int:
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum

print(summation_while(5)) # Expected output: 15
print(summation_for(5)) # Expected output: 15
