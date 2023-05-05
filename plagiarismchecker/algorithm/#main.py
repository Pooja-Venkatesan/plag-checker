from nltk.corpus import stopwords
from plagiarismchecker.algorithm import webSearch
import sys
import re

from termcolor import colored

# Given a text string, remove all non-alphanumeric
# characters (using Unicode definition of alphanumeric).
text = ''
def getQueries(text, n):
    sentenceEnders = re.compile("['.,()/!?]")
    sentenceList = sentenceEnders.split(text)
    sentencesplits = []
    en_stops = set(stopwords.words('english'))

    for sentence in sentenceList:
        x = re.compile(r'\W+', re.UNICODE).split(sentence)
        for word in x:
            if word.lower() in en_stops:
                x.remove(word)
        x = [ele for ele in x if ele != '']
        sentencesplits.append(x)
    finalq = []
    for sentence in sentencesplits:
        l = len(sentence)
        if l > n:
            l = int(l/n)
            index = 0
            for i in range(0, l):
                finalq.append(sentence[index:index+n])
                index = index + n-1
                if index+n > l:
                    index = l-n-1
            if index != len(sentence):
                finalq.append(sentence[len(sentence)-index:len(sentence)])
        else:
            if l > 4:
                finalq.append(sentence)
    return finalq


# def findSimilarity(text):
#     # n-grams N VALUE SET HERE
#     n = 15
#     queries = getQueries(text, n)
#     print('GetQueries task complete')
#     q = [' '.join(d) for d in queries]
#     output = {}
#     c = {}
#     i = 1
#     while("" in q):
#         q.remove("")
#     count = len(q)
#     if count > 100:
#         count = 100
#     numqueries = count
#     for s in q[0:count]:
#         output, c, errorCount = webSearch.searchWeb(s, output, c)
#         print('Web search task complete')
#         numqueries = numqueries - errorCount
#         # print(output,c)
#         sys.stdout.flush()
#         i = i+1
#     totalPercent = 0
#     outputLink = {}
#     websiteMatches = {} # new dict to track website matches
#     prevlink = ''
#     for link in output:
#         percentage = (output[link]*c[link]*100)/numqueries
#         percentage = round(percentage, 2)
#         if percentage > 10:
#             totalPercent = totalPercent + percentage
#             prevlink = link
#             outputLink[link] = percentage
#             websiteMatches[link] = [] # initialize list for current website
#             for j, query in enumerate(queries):
#                 if webSearch.isMatch(query, link):
#                     websiteMatches[link].append(j) # add matching sentence index
#         elif len(prevlink) != 0:
#             totalPercent = totalPercent + percentage
#             outputLink[prevlink] = outputLink[prevlink] + percentage
#         elif c[link] == 1:
#             totalPercent = totalPercent + percentage
#         totalPercent = round(totalPercent, 2)
#         print(link, totalPercent)

#     print(count, numqueries)
#     print(totalPercent, outputLink)
#     print("\nDone!")
#     return totalPercent, outputLink, websiteMatches, text

tracker ={}
totalPercent = 0
uniquePercent = 0
outputLink = {}
def findSimilarity(text):
    # n-grams N VALUE SET HERE
    n = 15
    queries = getQueries(text, n)
    print("queries")
    print(queries)
    print('GetQueries task complete')
    q = [' '.join(d) for d in queries]
    output = {}
    c = {}
    s = ''
    i = 1
    while("" in q):
        q.remove("")
    count = len(q)
    if count > 100:
        count = 100
    numqueries = count
    print("q")
    print(q)
    tracker={}
    for s in q[0:count]:
        print("s")
        print(s)
        highlighted_text = colored(s, 'red', attrs=['underline', 'bold'])
        print(highlighted_text)
        output, c, errorCount = webSearch.searchWeb(s, output, c)
        print('Web search task complete')
        tracker[s]=c
        numqueries = numqueries - errorCount
        print(output,c,errorCount)
        sys.stdout.flush()
        i = i+1
    totalPercent = 0
    uniquePercent = 0
    outputLink = {}
    print("output, c")
    print(output, c)
    prevlink = ''
    for link in output:
        percentage = (output[link]*c[link]*100)/numqueries
        percentage = round(percentage, 2)
        if percentage > 10:
            totalPercent = totalPercent + percentage
            prevlink = link
            outputLink[link] = percentage
        elif len(prevlink) != 0:
            totalPercent = totalPercent + percentage
            outputLink[prevlink] = outputLink[prevlink] + percentage
        elif c[link] == 1:
            totalPercent = totalPercent + percentage
        totalPercent = round(totalPercent, 2)
        uniquePercent = (100 - totalPercent)
        uniquePercent = round(uniquePercent,2)
        print(link, totalPercent, uniquePercent)

        print("\n OUTPUT LINKS:\t", outputLink)

    print("count", "numqueries")
    print(count, numqueries)
    # print("totalPercent","uniquePercent", "outputLink")
    # print(totalPercent,uniquePercent, outputLink)
    print("\nDone!")
    print("\nTracker!")
    print(tracker)
    plag_content = list(tracker.keys())
    links = list(outputLink.keys())
    scores = list(outputLink.values())
    print("\n Similar Text:",plag_content)
    print("\n list of links:", links)
    print("\n list of scores:", scores)
    return totalPercent, uniquePercent, links, scores, text, tracker
    # return totalPercent, uniquePercent, outputLink, text, tracker


    
# ...........
# text = "This is some text to highlight"
# highlighted_text = colored(s, 'red', attrs=['underline', 'bold'])
# print(highlighted_text)


