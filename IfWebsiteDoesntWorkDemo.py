import StackExchangeAPI
import DictionarySearch
import RandomDuckTalk

print(RandomDuckTalk.duckTalk())

print("What's your problem? (input comma separated keywords)")
search = input()
print("\n")

print("The top Ducktionary result is:")
print("\n")
print(DictionarySearch.runDictionarySearch(search))
print("\n")

print("Here are some other resources...")
print("\n")
response = StackExchangeAPI.getResults(search)

if len(response['items']) < 3:
    length = len(response['items'])
else:
    length = 3

for i in range(length):
    print((response["items"][i]['title']))
    print((response["items"][i]["link"]))
    print("\n")