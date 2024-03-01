def char_count_while(target:str, c:str) -> str:
    count = 0
    i = 0
    while i < len(target):
        if target[i] == c:
            count += 1
        i += 1
    return count

def char_count_for(target:str, c:str) -> str:
    count = 0
    for i in range(len(target)):
        if target[i] == c:
            count += 1
    return count

def char_count_foreach(target:str, c:str) -> str:
    count = 0
    for char in target:
        if char == c:
            count += 1
    return count

s = "hello"
c = "l"

num_times_c_in_s = char_count_foreach(s, c)
times_c_in_s = char_count_while(s, c)
c_in_s = char_count_for(s, c)

print(num_times_c_in_s) # Expected output: 2
print(times_c_in_s) # Expected output: 2
print(c_in_s) # Expected output: 2
