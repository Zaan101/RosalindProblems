with open('rosalind_revc.txt', 'r') as file:
    data = file.read().replace('\n', '')
new = ""
data = data[::-1]
for i, c in enumerate(data):
    if c== "A":
        new += "T"
    if c == "T":
        new += "A"
    if c== "G":
        new += "C"
    if c == "C":
        new +="G"
print(new)