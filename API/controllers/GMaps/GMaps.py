from flask import request
from json import dumps

from API.models.GMaps.itineraryGenerator import itineraryGenerator


def getTraject():

    # testing values
    origin = "Paris,FR"
    destination = "Houdan,FR"

    if('wayPoints' in request.form):
        baseUrl = itineraryGenerator.createTraject(origin, destination, wayPoints)
    else:
        baseUrl = itineraryGenerator.createTraject(
            origin,
            destination
        )

    data = itineraryGenerator.sendRequest(baseUrl)

    return dumps(data)
