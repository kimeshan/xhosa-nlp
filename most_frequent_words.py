import nltk
from nltk.probability import FreqDist
import csv

print("Opening file with 10 000 Xhosa sentences...")
#sentences_file = open('sample.txt', 'rU')
sentences_file = open('xhosa_2015_sentences.txt', 'rU')
print("File opened")

all_words = []

print("Start tokenizing sentences...")
for line in sentences_file:
    words = nltk.word_tokenize(line)
    words = [word.lower() for word in words if word.isalpha()]
    all_words.extend(words)

print("Total words: {0}".format(len(all_words)))

max = 500
fdist = FreqDist(all_words)
most_frequent = fdist.most_common(max)

with open('./results.csv', 'w') as out:
    writer = csv.writer(out)
    writer.writerow(["word", "frequency"])
    for idx, row in enumerate(most_frequent):
        writer.writerow([row[0], row[1]])

print("{0} most frequent words written to {1}".format(max, "results.csv"))
