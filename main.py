
from collections import Counter
#1
file = open("D:\data.txt", "rt")
data = file.read()
words = data.split()
print('Number of words in text file :', len(words))
#2
file = open("D:\data.txt", "rt")
count=0
line=file.readline()
while line!='':
      count+=1
      line=file.readline()
print('Number of lines in text file :',count)

#3
file = open("D:\data.txt", "rt")
data = file.read()
words1 = data.split()
count1=0
allwords= Counter()
for word in words1:
    allwords[word] += 1
for x in allwords:
      if allwords[x]==1:
            count1+=1
print('Number of unique words in text file :',count1)


#4.1
file = open("D:\data.txt", "rt")
sentence=file.read()
words2 = sentence.split()
f=len(words2)
file = open("D:\data.txt", "rt")
sentence=file.read()
sentences=sentence.split('.')
v=len(sentences)
print('the average lenth of the sentences is:',f/v)

#4.2
max=0
for r in sentences:
    u=len(r.split())
    if u>max:
        max=u
print('the maximal lenth of the sentences is:',max)


#5
file = open("D:\data.txt", "rt")
allcolors=Counter()
colors=["black","white","brown","orange","blue","pink","yellow","grey","green","purple","red","gold","silver","light blue","transparent"]
txt=file.read()
some = txt.split()
for o in some:
    if o in colors:
        allcolors[o]+=1
for s in allcolors:
    print(s)
    print(allcolors[s])


#6
maxWithoutK=0
sequence=[]
amount=0
file = open("D:\data.txt", "rt")
data2=file.read()
tx=data2.split()
for t in tx:
    if "k" not in t:
       sequence+=t
       amount+=1
    else:
        if amount>maxWithoutK:
            maxWithoutK=amount
        sequence=""
        amount=0
print('The maximum length of the word sequence without the letter k is:',maxWithoutK)


file.close()

