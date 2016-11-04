class GMapsInterface():

    baseUrlDirection = "https://maps.googleapis.com/maps/api/directions/json?"
    baseUrlElevation = "https://maps.googleapis.com/maps/api/elevation/"

    def __init(self):
        with open(PARENT_DIR + "API/config/configMaps.json") as data_file:
            data = json.load(data_file)
            validUrlDirection = self.baseUrlDirection + data["API_Key"]
            validUrlElevation = self.baseUrlElevation + data["API_Key"]

    def getDirectionUrl(self):
        return self.validUrlDirection

    def getElevationUrl(self):
        return self.validUrlDirection
