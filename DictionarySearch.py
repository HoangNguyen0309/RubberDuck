locationOfDictionary = "LocalSearchFrom.txt"


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

        word = line[0: line.index("-")]
        definition = line[line.index("-") + 1:]

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
        tags = tags[tags.index(",") + 1:]

    if (len(tags) > 0) & ("," in tags):
        tag2 = tags[0:tags.index(",")]
        tags = tags[tags.index(",") + 1:]

    if (len(tags) > 0) & ("," in tags):
        tag3 = tags[0:tags.index(",")]
        tags = tags[tags.index(",") + 1:]

    if (len(tags) > 0) & ("," in tags):
        tag4 = tags[0:tags.index(",")]
        tags = tags[tags.index(",") + 1:]

    if (len(tags) > 0) & ("," in tags):
        tag5 = tags[0:tags.index(",")]
        tags = tags[tags.index(",") + 1:]

    tagList = [tag1, tag2, tag3, tag4, tag5]
    # end of isolating tags

    # initialize the costs array
    for i in range(len(defs)):
        scores.append(0.0)

    for i in range(len(defs)):
        for k in range(len(tagList)):
            if tagList[k] in defs[i].word.lower():
                scores[i] += (len(tagList[k]) / len(defs[i].word))
    return scores


class Entries:
    word = ""
    definition = ""
    source = ""


    def __init__(self, word, definition, source):
        self.word = word
        self.definition = definition
        self.source = source


