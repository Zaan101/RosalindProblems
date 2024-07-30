with open('rosalind_dna.txt', 'r') as file:
    data = file.read().replace('\n', '')

a= [0] *4
for i, v in enumerate(data):
    if v == "A":
        a[0] =a[0]+1
    if v == "C":
        a[1] = a[1] + 1
    if v == "G":
        a[2] = a[2]+1
    if v == "T":
        a[3]= a[3]+1

print(a[0]," ",a[1]," ",a[2]," ",a[3])