import requests
import json


def api_call():
    api_url1 = "http://ergast.com/api/f1/current/results.json"
    api_url2 = "http://ergast.com/api/f1/current/next.json"

    current = requests.get(api_url1)
    next = requests.get(api_url2)

    filename = "current_results.json"
    page = open(filename, "w")
    text = json.dumps(current.json())
    page.write(text)
    page.close()
    print("Content has been written to: " + filename)

    filename = "next_round.json"
    page = open(filename, "w")
    text = json.dumps(next.json())
    page.write(text)
    page.close()
    print("Content has been written to: " + filename)

    season = str(current.json()["MRData"]["RaceTable"]["season"])

    return [season]
