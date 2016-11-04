import os
import http.client
import json
import math
from API.controllers.GMaps.GMaps import getTraject
from flask import request
from json import dumps
from random import choice

from API import app


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

    connection.close()
    return dumps({"pokemons": result})


def get():
    cities = ['marseille', 'berlin', 'moscou', 'varsovie', 'bamako', 'kigali', 'Ouagadougou', 'dubai']

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

        stages = [stage1, stage2, stage3]
        # Point de départ : request.form['start']
        # Etape 1, 2 et 3 : stage1, stage2, stage3
        # Destination : request.form['end']






        # user Google Map
        googleResult = getTraject(request.form["start"], request.form['end'], stages)
        traject = json.loads(googleResult)
        # Make Pokemon Calcul
        pokemon = getPokemon(request.form["pokemonId"])
        dictPokemon = json.loads(pokemon)
        numberPokemon = math.ceil(int(request.form["weight"])*5 / int(dictPokemon["pokemons"]["weight"]))

        # TODO Adapt googleTravelTime to real var; Distance var too
        # distance in meter
        distance = traject['routes'][0]['legs'][0]['distance']['value']
        timeTravel = int(distance)/1000 / int(dictPokemon["pokemons"]['speed'])

        result = {}

        result['namePokemon'] = dictPokemon["pokemons"]['name']
        result['numberPokemon'] = numberPokemon # number pokemon necessary to carry the user
        result['timeTravel'] = timeTravel # in hours
        result['distance'] = distance  # in meter
        result['stage'] = stages
        result['start'] = traject['routes'][0]['legs'][0]['start_address']
        result['end'] = traject['routes'][0]['legs'][0]['end_address']

        return dumps({'result': result}), 201







    else:
        return dumps({
            "success": False,
            "message": "Missing parameters"
        }, indent=4)