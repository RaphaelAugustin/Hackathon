from API.models.GMaps.interface import GMapsInterface
from urllib import request
import json


class itineraryGenerator():

    def __init(self):
        return self

    @staticmethod
    def createTraject(originId, destinationId, wayPoints=""):
        baseUrl = GMapsInterface.getDirectionUrl() + "origin=" + originCity + "destination=" + destinationCity

        if(len(wayPoints) != 0):
            for index, value in enumerate(wayPoints):
                if(index == len(wayPoints)):
                    wayPoints = wayPoints + value
                else:
                    wayPoints = wayPoints + "|" + value

            baseUrl = baseUrl + wayPoints

        return baseUrl

    def sendRequest(Url):
        webUrl = request.openUrl(Url)
        data = webUrl.read()
        encoding = webUrl.info().get_content_charset('utf-8')
        returnValue = json.loads(data.decode(encoding))
        return returnValue
