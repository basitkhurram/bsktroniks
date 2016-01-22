import random

def parser(fname):
    fhandler = open(fname, "r")
    words = []
    for line in fhandler.readlines():
        if line != "\n":
            aux_line = line.split()
            for word in aux_line:
                words.extend([word.strip("[").strip("(").strip("'").strip('"').strip("'").strip('"').strip(",").strip(".").strip("?").strip("!").strip(")").strip("]").lower()])
    fhandler.close()
    return words

def predictor(words):
    limit = len(words) - 1
    counter = 0
    dictionary = {}
    while counter < limit:
        word = words[counter]
        next_word = words[counter + 1]
        if word in dictionary:
            dictionary[word].append(next_word)
        else:
            dictionary[word] = [next_word]
        counter += 1
    return dictionary

def builder(dictionary, size):
    word = random.sample(list(dictionary), 1)[0]
    output = " " + word
    for n in range(200):
        output += " "
        word = random.choice(dictionary[word]).lower()
        output += word
        if n % 7 == 0:
            output += "\n"
    return output


#Initialize the training material to song 66 (arbitrary)
fname = "mash/66.txt"
words_comp = parser(fname)

#Songs are in mash folder.
#Songs are enumerated to help index
#the training material.

#Enumeration need not be contiguous.
#For example, certain songs/albums can be
#commented out to exclude them from
#the training material.

training = {
    # "cyrus, bangerz":  (1, 16),
    "muse, absolution":(17, 29),
    "ts, ts, select":  (30, 43),
    "ratm, ratm":      (44, 53),
    # "muse, drones":    (54, 65),    
    "rh, httt":        (66 + 1, 83),
    "rh, ir":          (84, 99),
    # "coldplay, xy":    (100, 113)    
    }

for album in training:
    start, end = training[album]
    for n in range(start, end + 1):
        fname = "D:/python/bstroniks/mash/" + str(n) + ".txt"
        words_comp += parser(fname)
size = int(len(words_comp)/n)
dictionary = predictor(words_comp)
output = builder(dictionary, size)

foutput = open("test.txt", "w")
foutput.write(output)
foutput.close()
