import random

def parser(fname):
    fhandler = open(fname, "r")
    words = []
    for line in fhandler.readlines():
        if line != "\n":
            aux_line = line.split()
            #print(aux_line)
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
    #print(word)
    output = " " + word
    #print(type(dictionary))
    for n in range(200):
        output += " "
        #print(dictionary[word])
        word = random.choice(dictionary[word]).lower()
        output += word
        if n % 7 == 0:
            output += "\n"
    return output


fname = "D:/python/bstroniks/mash/66.txt"
words_comp = parser(fname)

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
##fname = "D:/python/bstroniks/samples/t4.txt"
##words = parser(fname)
##dictionary = predictor(words)
##output = builder(dictionary)
