locationOfDictionary = "LocalSearchFrom.txt"

# take a query and return dictionary results
def runDictionarySearch(tags):
    defs = []
    scores = []

    # go through the dictionary and create an object for each term and then add them to a list
    dict = open(locationOfDictionary, "r")
    numTrack = 1
    while True:

        line = dict.readline()

        if not line:
            break

        word = line[0: line.index("-") - 1]
        definition = line[line.index("-") + 2:]

        if numTrack < 125:
            source = "https://stackify.com/java-glossary"
        if numTrack > 124 & numTrack < 137:
            source = "https://www.geeksforgeeks.org/types-of-exception-in-java-with-examples/"
        if numTrack > 136 & numTrack < 140:
            source = "https://curc.readthedocs.io/en/latest/programming/coding-best-practices.html"
        if numTrack > 139 & numTrack < 232:
            source = "https://www.coursereport.com/blog/coding-jargon-glossary-of-key-terms-at-coding-bootcamp"
        if numTrack < 1 | numTrack > 231:
            source = "Source not available"

        defs.append(Entries(word, definition, source))
        numTrack = numTrack + 1
    # end of creating objects

    # isolate the tags
    tags = tags.lower() + ","
    tag1 = " "
    tag2 = " "
    tag3 = " "
    tag4 = " "
    tag5 = " "

    if (len(tags) > 0) & ("," in tags):
        tag1 = tags[0:tags.index(",")]
        tags = tags[tags.index(",") + 2:]

    if (len(tags) > 0) & ("," in tags):
        tag2 = tags[0:tags.index(",")]
        tags = tags[tags.index(",") + 2:]

    if (len(tags) > 0) & ("," in tags):
        tag3 = tags[0:tags.index(",")]
        tags = tags[tags.index(",") + 2:]

    if (len(tags) > 0) & ("," in tags):
        tag4 = tags[0:tags.index(",")]
        tags = tags[tags.index(",") + 2:]

    if (len(tags) > 0) & ("," in tags):
        tag5 = tags[0:tags.index(",")]
        tags = tags[tags.index(",") + 2:]

    tagList = [tag1, tag2, tag3, tag4, tag5]
    # end of isolating tags

    # initialize the costs array
    for i in range(len(defs)):
        scores.append(0.0)
    # end initialize cost

    # increase the score based on a keywords percent match to the word
    for i in range(len(defs)):
        for k in range(len(tagList)):
            if tagList[k] != " ":
                if tagList[k] in defs[i].word.lower():
                    scores[i] += (len(tagList[k]) / len(defs[i].word)) * 1.5
                else:
                    numCharsInWord = 0
                    for q in range(len(tagList[k])):
                        if tagList[k][q] in defs[i].word.lower():
                            numCharsInWord += 1
                    scores[i] += (numCharsInWord / len(defs[i].word)) * 0.15
    # end increase from word match

    # increase the score based on the number of keywords in the definition
    for i in range(len(defs)):
        defScore = 0
        for k in range(len(tagList)):
            if tagList[k] != " ":
                if tagList[k] in defs[i].definition.lower():
                    defScore += 4
                else:
                    numCharsInWord = 0
                    for q in range(len(tagList[k])):
                        if tagList[k][q] in defs[i].definition.lower():
                            numCharsInWord += 1
                        defScore += (numCharsInWord / len(defs[i].definition)) * 0.5
        scores[i] += defScore * 0.1
    # end increase score from definition matches

    # sort the entries by score (bubble sort and move items in defs and scores, decreasing order
    x = len(defs)
    for i in range(x):
        for j in range(x - i - 1):
            if scores[j] > scores[j + 1]:
                scores[j], scores[j + 1] = scores[j + 1], scores[j]
                defs[j], defs[j + 1] = defs[j + 1], defs[j]
    defs = list(reversed(defs))
    # end sort by score

    # return top result in String format
    return (defs[0].word + "\n" + defs[0].definition + defs[0].source)
# end method

class Entries:
    word = ""
    definition = ""
    source = ""


    def __init__(self, word, definition, source):
        self.word = word
        self.definition = definition
        self.source = source


