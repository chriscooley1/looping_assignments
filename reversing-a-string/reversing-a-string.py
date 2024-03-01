def reverse_while(s:str) -> str:
    reversed_str = ""
    i = len(s) - 1
    while i >= 0:
        reversed_str += s[i]
        i -= 1
    return reversed_str

def reverse_for(s:str) -> str:
    reversed_str = ""
    for i in range(len(s) - 1, -1, -1):
        reversed_str += s[i]
    return reversed_str

def reverse_foreach(s:str) -> str:
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str

s = "hello"

r = reverse_while(s)
q = reverse_for(s)
p = reverse_foreach(s)

print(r) # Expected output: "olleh"
print(q) # Expected output: "olleh"
print(p) # Expected output: "olleh"
