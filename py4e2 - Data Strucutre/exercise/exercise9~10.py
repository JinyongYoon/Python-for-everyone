# get method
people = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names :
    people[name] = people.get(name, 0) + 1
print(people)

# example
name = input('Enter file:')
handle = open(name)

counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1

bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword, bigcount)

# Exercise9.4
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
    
handle = open(name)

counts = dict()
for line in handle:
    if line.startswith('From '):
        words = line.split()
        word = words[1] 
        counts[word] = counts.get(word,0) + 1

bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword, bigcount)

#Tuple sorting example
c = {'a':10, 'b':1, 'c':22}
tmp = list()
for k, v in c.items() :
    tmp.append((v, k))

tmp = sorted(tmp)
print(tmp)

#List comprehension
c = {'a':10, 'b':1, 'c':22}
print( sorted( [ (v,k) for k,v in c.items() ] ) )

# Exercise10.2
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
    
handle = open(name)

counts = dict()
for line in handle:
    if line.startswith('From '):
        words = line.split()
        word = words[5]
        hours = word.split(":")
        hour = hours[0]
        counts[hour] = counts.get(hour,0) + 1

counts = sorted(counts.items())
for hour,count in counts:
    print(hour, count)