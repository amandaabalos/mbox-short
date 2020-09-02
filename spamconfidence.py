#import regular expression library
import re

hand=open('mbox-short.txt')

#create a list function in numlist
numlist=list()

#for index in hand
for line in hand:
    #strip out any spaces on the right of line
    line=line.rstrip()

    #find all lines that start with X-SPAM-Confidence: any numbers 0-9 however many times
    stuff=re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)
    #if length of stuff is not 1, go back up to loop and start again
    if len(stuff) != 1: continue
    #create variable num and store stuff index 0 as a float
    num=float(stuff[0])
    #append num to a list
    numlist.append(num)
#print max
print('Maximum:', max(numlist))
