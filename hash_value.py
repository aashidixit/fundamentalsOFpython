import random
Alphabets="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
print(Alphabets)
      
Strings=[]
for j in range (1000):
    length= random.randint(2,10)
    blkstr=""
    for i in range (0,length):
        randno= random.randint(0,61)
        blkstr+=Alphabets[randno]
        Strings.append(blkstr)
print(blkstr)
print(Strings)
asciival={}
asc=65     
for char in Alphabets[0:26]:
    asciival[char]=asc
    asc+=1
    
asc=97
for char in Alphabets[26:52]:
    asciival[char]=asc
    asc+=1
      
asc=48
for char in Alphabets[52:62]:
    asciival[char]=asc
    asc+=1
      
print(asciival)
hashvalue=0
primeno=13
power=1
blkstr=[]           
         
for i in range (1000):
    power=1 
    hashvalue=0
    for char in Strings[i]:
        hashvalue+=asciival[char]*primeno**power
        power+=1
        blkstr.append(hashvalue)
data = {}
for char,hashvalue in zip(Strings,blkstr):
    try:
        temp = data[hashvalue]
    except:
        temp = 0
    data[hashvalue] = temp + 1
print(data)
for k in range(len(blkstr)):
      for l in range(len(blkstr)-1-k):
          if(blkstr[l]>blkstr[l+1]):
              temp=blkstr[l]
              blkstr[l]=blkstr[l+1]
              blkstr[l+1]=temp


import matplotlib.pyplot as plt
plt.figure(figsize=(50,10))
plt.bar(range(len(data)), data.values(), align='center')
plt.xticks(range(len(data)), data.keys())

