from API.models.GMaps.interface import GMapsInterface
from urllib import request
import json


class itineraryGenerator():

    def __init(self):
        return self

    def createTraject(origin, destination, wayPoints):
        GMaps = GMapsInterface()
        baseUrl = str(GMaps.validUrlDirection) + "&origin=" + str(origin) + "&destination=" + str(destination) + "&waypoints="

        if(len(wayPoints) != 0):
            wayPointString = ""
            for value in wayPoints:
                if(value == wayPoints[len(wayPoints)-1]):
                    wayPointString += "via:" + value
                else:
                    wayPointString += "via:" + value + "|"

            baseUrl = baseUrl + wayPointString

        return baseUrl

    def sendRequest(Url):

        print(Url)
        req = request.Request(str(Url))
        response = request.urlopen(req)
        data = response.read()
        returnValue = json.loads(data.decode())
        return returnValue
