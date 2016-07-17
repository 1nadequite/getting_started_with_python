# common words

# get the name of the file and open it
name = raw_input('Enter file:')
handle = open(name, 'r')
text = handle.read()
words = text.split()

# count word frequency
counts = dict()
for word in words:
     counts[word] = counts.get(word,0) + 1
bigcount = None
bigword = None

#fint the most common word
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

#all done
print bigword, bigcount
