import random
import sys
import os.path
import json


def loadData(name):
    with open(name + '.json', 'r') as f:
        return json.load(f)


def saveData(obj, name):
    with open(name + '.json', 'w') as f:
        json.dump(obj, f, sort_keys=True, indent=4)


def loadText(name):
    with open( name, 'r') as f:
        data = f.read().replace('\n', ' ')
        return data.split()


def generateMarkovChain(text):
    ngrams = {}
    beginnings = []

    for c, gram in enumerate(text):

        if (c >= len(text) - 1):
            break

        if (gram not in ngrams):  # if the ngram is not found in the dic create an array for it
            ngrams[gram] = []

        if ('.' in gram and c < len(text) - 1):
            beginnings.append(text[c + 1])
        ngrams.setdefault(gram, []).append(text[c + 1])  # add the word that comes after the ngram

    saveData(ngrams, "Markov_Chain/chain")
    saveData(beginnings, "Markov_Chain/beginnings")


def generateText(ngrams, beginnings, max):
    currentGram = random.choice(beginnings)
    result = [currentGram]

    for i in xrange(0, max):
        try:
            possibilities = ngrams[currentGram]

            if (possibilities is not None):
                result.append(' ' + random.choice(ngrams[currentGram]))
                currentGram = result[-1]
                currentGram = currentGram.strip()

        except:
            print("Chain ran dry")
            print(currentGram)
            break
    return " ".join(result)


def main():
    file_name = "Scraped_TLS/tweets.txt"  # change to what ever data set you want
    response_len = 5  # this will determine the output length

    data = loadText(file_name)

    if os.path.isfile("/Markov_Chain/chain.json") is False:
        print("Could not find markovchain generating a new one")
        generateMarkovChain(data)

    markovchain = loadData("Markov_Chain/chain")
    beg = loadData("Markov_Chain/beginnings")

    print("Chain loaded properly")

    print(generateText(markovchain, beg, response_len))


if __name__ == "__main__":
    main()
