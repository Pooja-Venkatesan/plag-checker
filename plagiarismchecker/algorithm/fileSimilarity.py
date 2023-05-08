import re
import math
from nltk.corpus import stopwords

def calculateTF(wordlist):
    tf = {}
    for word in wordlist:
        tf[word] = tf.get(word, 0) + 1
    return tf

def calculateDotProduct(tf1, tf2):
    dotProduct = 0
    for word, count1 in tf1.items():
        if word in tf2:
            count2 = tf2[word]
            dotProduct += count1 * count2
    return dotProduct

def calculateMagnitude(tf):
    magnitude = 0
    for count in tf.values():
        magnitude += count ** 2
    return math.sqrt(magnitude)

def findFileSimilarity(inputText1, inputText2):
    wordlist1 = []
    wordlist2 = []

    lowercaseText1 = inputText1.lower()
    lowercaseText2 = inputText2.lower()
    en_stops = set(stopwords.words('english'))

    # Replace punctuation by space and split
    wordlist1 = re.sub("[^\w]", " ", lowercaseText1).split()
    wordlist2 = re.sub("[^\w]", " ", lowercaseText2).split()

    # Remove stopwords
    wordlist1 = [word for word in wordlist1 if word not in en_stops]
    wordlist2 = [word for word in wordlist2 if word not in en_stops]

    # Calculate TF for wordlist1 and wordlist2
    tf1 = calculateTF(wordlist1)
    tf2 = calculateTF(wordlist2)

    # Calculate dot product
    dotProduct = calculateDotProduct(tf1, tf2)

    # Calculate magnitudes
    magnitude1 = calculateMagnitude(tf1)
    magnitude2 = calculateMagnitude(tf2)

    # Calculate total percentage using TF algorithm
    totalPercent = (dotProduct / (magnitude1 * magnitude2)) * 100
    totalPercent = round(totalPercent, 2)
    uniquePercent = 100 - totalPercent
    uniquePercent = round(uniquePercent,2)
    print ('wordlist1 :',wordlist1)
    print()
    print('\n wordlist2 :',wordlist2)
    print ('\n input1TF :',tf1)
    print ('\n input2TF :',tf2)

    return totalPercent, uniquePercent, wordlist1, wordlist2
