def list_multiply_while(a: list[int], b: list[int]) -> list[int]:
    total = []
    i = 0
    while i < len(a):
        total.append(a[i] * b[i])
        i += 1
    return total

def list_multiply_for(a: list[int], b: list[int]) -> list[int]:
    total = []
    for i in range(len(a)):
        total.append(a[i] * b[i])
    return total

a = [1, 2, 3]
b = [4, 5, 6]

c = list_multiply_while(a, b)  # This should compute [1*4, 2*5, 3*6]
print(c)  # Expected output: [4, 10, 18]

c = list_multiply_for(a, b)
print(c) # Expected output: [4, 10, 18]
