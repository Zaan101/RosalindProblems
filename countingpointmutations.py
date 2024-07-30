with open('rosalind_hamm.txt', 'r') as file:
    data= file.read()

first, second = data.split()


count = 0

for i, c in zip(first, second):
    if i != c:
        count += 1
print(count)

