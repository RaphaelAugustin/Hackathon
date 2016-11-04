from flask import request
from json import dumps

from API.models.GMaps.itineraryGenerator import itineraryGenerator


def getTraject(origin, destination, wayPoints):

    baseUrl = itineraryGenerator.createTraject(origin, destination, wayPoints)

    data = itineraryGenerator.sendRequest(baseUrl)

    return dumps(data)
