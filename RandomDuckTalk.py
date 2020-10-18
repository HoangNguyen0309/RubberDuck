import random

fileName = "duckhelp.txt"

def duckTalk():
    phrases = open(fileName, "r")
    lines = phrases.readlines()
    return(lines[random.randint(0, len(lines) - 1)])
