counts = dict()
print('Enter a line: ')
line=input('')

words=line.split()

print('Words:', words)

print('counting...')
for word in words:
    counts[word]=counts.get(word,0)+1
print('Counts', counts)
