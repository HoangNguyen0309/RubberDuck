import requests
import json
import sys


class Results:

    def getResults(tags):

        # replace the spaces with underlines
        tags = Results.getUsableTags(tags)

        # add a comma to the end of tags to prevent crashing and initialize individual tags
        tags = tags + ","
        tag1 = " "
        tag2 = " "
        tag3 = " "
        tag4 = " "
        tag5 = " "

        # isolate each tag by spaces
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

        # create the url from the tags that the API will collect
        tagSplit = "%3B%20"
        buildURL = ("https://api.stackexchange.com/2.2/tags/" + tag1 + tagSplit + tag2 + tagSplit + tag3 + tagSplit +
                    tag4 + tagSplit + tag5 + "/faq?site=stackoverflow")

        # url for testing, no longer needed
        testURL = "https://api.stackexchange.com/2.2/tags/java%3B%20exception%3B%20FileNotFoundException/" \
                  "faq?site=stackoverflow"

        # get the response from the API and save it as a JSON object
        url = buildURL
        response = requests.get(url)
        responseJSON = response.json()

        # For testing, print all of the results' link and title
        """
        for i in range(len(responseJSON['items'])):
           print((responseJSON['items'][i]['title']))
           print((responseJSON['items'][i]['link']))
        """

        # return the JSON object
        return responseJSON

    # replaces the spaces with underlines
    def getUsableTags(tags):
        workingTags = ""
        originalTag = tags
        for i in range(len(tags)):
              if originalTag[i] == " ":
                  workingTags = workingTags + "_"
              else:
                  workingTags = workingTags + originalTag[i]
        return workingTags
