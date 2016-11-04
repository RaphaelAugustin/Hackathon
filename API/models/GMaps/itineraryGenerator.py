from API.models.GMaps.interface import GMapsInterface
from urllib import request
import json


class itineraryGenerator():

    def __init(self):
        return self

    def createTraject(origin, destination, wayPoints=""):
        GMaps = GMapsInterface()
        baseUrl = str(GMaps.validUrlDirection) + "&origin=" + str(origin) + "&destination=" + str(destination)

        if(len(wayPoints) != 0):
            for index, value in enumerate(wayPoints):
                if(index == len(wayPoints)):
                    wayPoints = wayPoints + value
                else:
                    wayPoints = wayPoints + "|" + value

            baseUrl = baseUrl + wayPoints

        return baseUrl

    def sendRequest(Url):

        req = request.Request(str(Url))
        response = request.urlopen(req)
        data = response.read()
        returnValue = json.loads(data.decode())
        return returnValue
