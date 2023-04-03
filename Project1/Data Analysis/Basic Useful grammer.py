# enumerate
a = [111,222,333,444,555]
mapping = {}
for key, value in enumerate(a):
    mapping[key] = value
print(mapping)

# zip & enumerate
seq1 = ['foo', 'bar', 'baz']
seq2 = ['one', 'two', 'three']
zipped = list(zip(seq1,seq2))
print(zipped)

for i , (a,b) in enumerate(zip(seq1,seq2)):
    print(f'{i}: {a}, {b}')

# mapping using zip
pitchers = [('Nolan', 'Ryan'), ('Roger', 'Clemens'), ('Schilling', 'Curt')]
first_names, last_names = zip(*pitchers)
print(first_names)

# generate dic
mapping2 = dict(zip(range(5), reversed(range(5))))
print(mapping2)

# setdefault
words = ['apple', 'bat', 'bar', 'atom', 'book']
by_letter = {}
for word in words:
    letter = word[0]
    by_letter.setdefault(letter, []).append(word)
print(by_letter)