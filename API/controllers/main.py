import os
import http.client
import json
import math
from flask import request
from json import dumps
from random import choice

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
    result["weight"] = math.ceil(jsondata["weight"] / 10)
    for stat in jsondata['stats']:
        if stat['stat']["name"] == "speed":
            result["speed"] = math.ceil(stat["base_stat"] / 10)
            break

    print(result)
    connection.close()
    return dumps({"pokemons": result})


def get():
    cities = ['Baghdad', 'Hanoi', 'Los Angeles', 'Alexandria', 'Durban', 'Jakarta', 'Kinshasa', 'Dhaka', 'Kolkata', 'Riyadh', 'Seoul', 'Yokohama', 'Shenzhen', 'Yangon', 'Surat', 'New York City', 'Berlin', 'Ouagadougou']

    if (
        "weight" in request.form
        and "start" in request.form
        and "end" in request.form
        and "pokemonId" in request.form
    ):



        stage1 = choice(cities)

        stage2 = choice(cities)
        while stage2 == stage1:
            stage2 = choice(cities)

        stage3 = choice(cities)
        while stage3 == stage1 or stage3 == stage2:
            stage3 = choice(cities)

        # Point de départ : request.form['start']
        # Etape 1, 2 et 3 : stage1, stage2, stage3
        # Destination : request.form['end']

        return dumps({"success": True})

        pokemon = getPokemon(request.form["pokemonId"])

        numberPokemon = math.ceil(request.form['weight'] / pokemon['weight'])

        timeTravel = googleTravelTime / pokemon['speed']

        result = {}

        result['namePokemon'] = pokemon['name']
        result['numberPokemon'] = numberPokemon
        result['timeTravel'] = timeTravel
        result['distance'] = distance



        return dumps(result)



    else:
        return dumps({
            "success": False,
            "message": "Missing parameters"
        }, indent=4)