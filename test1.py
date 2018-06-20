a = ['1', '2', '3', '4', '5']
b = list(map(int, a))
print(b)

c = [int(x) for x in a if int(x) > 2]
print(c)

lis = [1, 2, 3, 3]
print(sum(lis))

print([2 * x + 1 for x in range(5) if x > 1])

rows = range(1, 4)
cols = range(1, 3)
cells = [(row, col) for row in rows for col in cols]
print(cells)

#{key_item:value_item for item in iterable}
'''word='letters'
letter_counts={letter:word.count(letter) for letter in word}
print(letter_counts)'''

word = 'letter'
letter_counts = {letter: word.count(letter) for letter in set(word)}
print(letter_counts)

a_set = {number for number in range(1, 6) if number % 3 == 1}
print(a_set)

number_thing = (number for number in range(1, 6))
print(number_thing)

for number in number_thing:
    print(number)

a = True
print(int(a))
