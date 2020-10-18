from flask import Flask, request

app = Flask(__name__)

import dictionary as dictionary
import requests
import json
import sys


def getResults(tags):
    # replace the spaces with underlines
    tags = getUsableTags(tags)

    # add a comma to the end of tags to prevent crashing and initialize individual tags
    tags = tags + ","
    tag1 = " "
    tag2 = " "
    tag3 = " "
    tag4 = " "
    tag5 = " "

    # isolate each tag by commas
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

    # For testing, print all of the results' title and link
    """
    for i in range(len(responseJSON['items'])):
       print((responseJSON['items'][i]['title']))
       print((responseJSON['items'][i]['link']))


    """


    return responseJSON

    import json
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(responseJSON, f, ensure_ascii=False, indent=4)


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

#this should be templated
@app.route('/')
def hello_world():
    return """<!DOCTYPE html>
<html lang="en">
<head>

	<title>RubberDuck</title>
	<script type="module" src="https://unpkg.com/@google/model-viewer/dist/model-viewer.min.js"></script>
    <!--<link rel="stylesheet" href="rubber.css" id="change">-->
</head>
<body style="background-color: #073763ff;">
	<!--<script src="duck.js"></script>-->
	<p1 id="press">
        
    </p1>
	<model-viewer src="duck.glb" camera-controls auto-rotate auto-rotate-delay=10000 rotation-per-second="45deg" interaction-prompt=none camera-orbit="45deg 80deg" shadow-intensity="0" onclick="myFunction()" class="center" class="space"></model-viewer>
    <h1 class="name" class="space">RubberDuck</h1>
    <form action="/info" method="post" novalidate>
	    <input  type="text" id="pEnter" class='input' name="tags" placeholder="What's your problem?">
	    <button>Send</button>
    </form>
    
</body>
</html>"""


@app.route('/new')
def OUT2():
    return """<!DOCTYPE html>
<html lang="en">
<head>
 <style>
		model-viewer {
			float: initial;
    		display: block;
    		margin-left: auto;
    		margin-right: auto;
    		width: 50%;
    		margin-top: 200px;
    		width: 240px;
    		height: 240px;
		}
		h1 {
			font-family: Montserrat;
    		font-size: 64px;
    		text-align: center;
    		color: white;
    		margin-top: 0px;
			margin-bottom: 24px;
    		font-weight: bold;
		}
		input {
			font-family: Montserrat;
    		border: none;
    		border-radius: 15px;
    		display: block;
    		width: 30%;
    		font-size: 16px;
    		float: center;
    		padding: 12px 20px;
    		margin: 0 auto;
    		margin-top: 2px; 
    		margin-bottom: 0px;
			
    		background-image: url('searchIcon.png');
    		background-position: 97%;
    		background-size: 12px 12px;
    		background-repeat: no-repeat;
		}
		input:focus {
    		background-color: lightblue;
    		border: none;
    		outline: none;
    		border-radius: 15px;
		}
		@font-face {
    		font-family: Mont;
    		src: url(Montserrat-Bold.ttf);
			font-weight: bold;
		}

	</style>
	<title>RubberDuck</title>
	<script type="module" src="https://unpkg.com/@google/model-viewer/dist/model-viewer.min.js"></script>
    <!--<link rel="stylesheet" href="rubber.css" id="change">-->
   
</head>
<body style="background-color: #073763ff;">
	<!--<script src="duck.js"></script>-->
	<p1 id="press">

    </p1>
	<model-viewer src="duck.glb" camera-controls auto-rotate auto-rotate-delay=10000 rotation-per-second="45deg" interaction-prompt=none camera-orbit="45deg 80deg" shadow-intensity="0" onclick="myFunction()" class="center" class="space"></model-viewer>
    <h1 class="name" class="space">RubberDuck</h1>
    <h1>this is page 2</h1>

</body>
</html>"""

@app.route('/info', methods=['GET', 'POST'])
def info():
    data = request.form["tags"]

    print(data)
    return getResults(data)

if __name__ == '__main__':
  app.run(debug=True)
