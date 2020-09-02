fhand=open('mbox-short.txt')

newlist=list()

for line in fhand:
    line=line.rstrip()
    if 'From ' in line:
        words=line.split()
        #print(words)
        ind=words[5]
        hr=ind.split(':')
        #print(hr[0])
        #count=count+1
        #print(ind)
        newlist.append(hr[0])
#print(newlist)

counts = dict()
for line in newlist:
    words=line.split()
    #print(words)
    for word in words:
        counts[word]=counts.get(word, 0)+1
#print(counts)

#counts.items()
count=counts.items()
sort=sorted(count)
#print(sort)

for k,v in sort:
    print(k,v)

#for i in sort:
#    lst.append(i)
#    print(lst)

#    word=lst[0,2]
#    print(word)






        #for hr in ind:
        #    wd=ind.split(':')
        #    print(wd[0])
        #    index=wd[0]
        #    #print(ind)
        #    count=count+1

        #    newlist.append(index)
        #print(newlist)
