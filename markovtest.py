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
        if(gram not in ngrams): #if the ngram is not found in the dic create an array for it 
            ngrams[gram]= []
        
        if(gram is '.' and c < len(text)-2):
            beginnings.append(ngram[c+2])
        ngrams[gram] += text[c+1] #add the charater that comes after the ngram
    saveData(ngrams,"chain")
    saveData(beginnings,"beginnings")



def generateText(text,ngrams,beginnings):

    currentGram = random.choice(beginnings) #start on the first word
    result = currentGram

    for i in xrange(0,100):
        try:
            possibiilities = ngrams[currentGram]

            if(possibiilities is not None):
                result += random.choice(ngrams[currentGram])
                currentGram = result[len(result)-n:len(result)]
                currentGram = currentGram.lower()
            
                
        except:
            print("Chain ran dry")
            print(currentGram)
            break
    return result
        



data = loadText("data.txt")

    

if(os.path.isfile("chain.json") is False):
    print("Could not find markovchain generating a new one")
    generateMarkovChain(data)

markovchain = loadData("chain")
beg = loadData("beginnings")

print("Chain loaded properly")

print(generateText(data,markovchain,beg))





