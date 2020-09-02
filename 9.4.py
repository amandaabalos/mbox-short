fhand = open('mbox-short.txt')
count=0
newlist=[]

for line in fhand:
    line=line.rstrip()
    if 'From ' in line:
        words=line.split()
        #print(words)
        ind=words[1]
        count=count+1
        #print(ind)
        newlist.append(ind)
#print (newlist)

counts = dict()
for line in newlist:
    words=line.split()
    for word in words:
        counts[word]=counts.get(word, 0)+1
#print(counts)

bigcount = None
bigword = None
for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
print(bigword, bigcount)


    #    counts=dict()
    #    for emails in ind:
    #        word=emails.split()
    #        for wd in word:
    #            counts[word]=counts.get(word,0)+1
    #        print(counts)
