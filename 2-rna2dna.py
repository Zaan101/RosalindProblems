with open('rosalind_rna.txt', 'r') as file:
    data = file.read().replace('\n', '')
print(data.replace("T","U"))
