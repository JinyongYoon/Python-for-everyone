# Exercise6.5
text = "X-DSPAM-Confidence:    0.8475"
start = text.find("0")
data = float(text[start+1 :])
print(data)

words = 'Hello World'
print(words[0:1])

# Exercise7.1
fhandle = open("/Users/jinyong/py4e/mbox-short.txt")
for line in fhandle:
    line = line.rstrip()
    print(line.upper())

# Exercise7.2
fname = input("Enter file name: ")
fhandle = open(fname)
count = 0
number = 0
for line in fhandle:
    if not line.startswith("X-DSPAM-Confidence:"): 
        continue
    count = count + 1
    start = line.find("0")
    number += float((line[start+1:]))

average = number / count
print("Average spam confidence:", average)

# Exercise8.4
fname = input("Enter file name: ")
fhandle = open(fname)
line = fhandle.read()

word = line.split()
word.sort()
primary_words = [] 
for i in word:
    if i not in primary_words: 
        primary_words.append(i) 
print(primary_words)

# Exercise8.5
fname = input("Enter file name: ")
if len(fname) < 1 : 
    fname = "mbox-short.txt"

count = 0
fh = open(fname)
for line in fh:
    if not line.startswith('From:'):
        continue
    count = count+1
    lines = line.split()
    print(lines[1])

print("There were", count, "lines in the file with From as the first word")

