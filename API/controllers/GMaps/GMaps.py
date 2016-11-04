import os
from flask import request
from json import dumps

from API import app
from API.models.GMaps import itineraryGenerator


def getTraject():
    generator = itineraryGenerator()

    if('wayPoints' in request.form):
        baseUrl = generator.createTraject(request.form['origin'], request.form['destination'], request.form['wayPoints'])
    else:
        baseUrl = generator.createTraject(request.form['origin'], request.form['destination'])

    data = itineraryGenerator.sendRequest(baseUrl)

    return dumps(data)
