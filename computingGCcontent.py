sequences = {}

with open("rosalind_gc.txt", 'r') as file:
    key = ""
    value = ""
    for line in file:
        if line.startswith('>'):
            if key:
                sequences[key] = value
            key = line[1:].strip()
            value = ""
        else:
            value += line.strip()
    if key:
        sequences[key] = value

max = ""
maxGC = 0
CGs = 0
for label, seq in zip(sequences.keys(),sequences.values()):
    for i, c in enumerate(seq):
        if c == "G" or c == "C":
            CGs += 1
    if CGs/len(seq) >= maxGC:
        maxGC = CGs/len(seq)
        max = label
    CGs = 0

print(max)
print(maxGC*100)


