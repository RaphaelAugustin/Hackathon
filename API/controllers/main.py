import os
import http.client
import json
from flask import request
from json import dumps

from API import app

#
# def get(pokeId):
#     return dumps({"pokemon number": pokeId})


def getPokemon(pokeId):
    connection = http.client.HTTPConnection("www.pokeapi.co")
    connection.request("GET", "/api/v2/pokemon/" + str(pokeId) + "/")
    response = connection.getresponse()
    data = response.read().decode('utf-8')

    jsondata = json.loads(data)

    result = {}
    result["name"] = jsondata["name"]
    result["weight"] = jsondata["weight"]
    for stat in jsondata['stats']:
        if stat['stat']["name"] == "speed":
            result["speed"] = stat["base_stat"]
            break

    print(result)
    connection.close()
    return dumps({"pokemons": result})

