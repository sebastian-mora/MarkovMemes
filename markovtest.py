import random
import sys
import os.path
import json



def loadData(name):
    with open(name + '.json', 'r') as f:
         return json.load(f)

def saveData(obj, name):
    with open(name + '.json','w') as f:
        json.dump(obj,f,sort_keys =True, indent=4)


def loadText(name):
    with open(name, 'r') as f:
        data = f.read().replace('\n', ' ')
        return data.split()


def generateMarkovChain(text):
    i=0
    ngrams = {}
    beginnings = []

    for c, gram in enumerate(text):

        if(c >= len(text)-1):
            break

        if(gram not in ngrams): #if the ngram is not found in the dic create an array for it 
            ngrams[gram]= []
        
        if( '.' in gram and c < len(text)-1):
            beginnings.append(text[c+1])
        ngrams.setdefault(gram,[]).append(text[c+1]) #add the word that comes after the ngram
    saveData(ngrams,"chain")
    saveData(beginnings,"beginnings")



def generateText(ngrams,beginnings):

    currentGram = random.choice(beginnings)
    result = [currentGram]

    for i in xrange(0,15):
        try:
            possibilities = ngrams[currentGram]

            if(possibilities is not None):
                result.append(' ' + random.choice(ngrams[currentGram]))
                currentGram = result[-1]
                currentGram = currentGram.strip()
            
                
        except:
            print("Chain ran dry")
            print(currentGram)
            break
    return " ".join(result)
        



data = loadText("data.txt")

    

if(os.path.isfile("chain.json") is False):
    print("Could not find markovchain generating a new one")
    generateMarkovChain(data)

markovchain = loadData("chain")
beg = loadData("beginnings")

print("Chain loaded properly")

print(generateText(markovchain,beg))





