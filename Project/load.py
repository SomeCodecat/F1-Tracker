import json
from api import api_call

#stats = api_call()


def jsonRequest():
    f = open("current_results.json")
    stats = json.load(f)

    season = stats["MRData"]["RaceTable"]["season"]
    round = stats["MRData"]["RaceTable"]["round"]

    return[season, round]
