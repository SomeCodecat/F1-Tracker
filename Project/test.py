import json
from api import api_call

#stats = api_call()


f = open("current_results.json")
stats = json.load(f)

season = stats["MRData"]["RaceTable"]["season"]

print(len(stats["MRData"]["RaceTable"]["Races"][0]["Results"]))
