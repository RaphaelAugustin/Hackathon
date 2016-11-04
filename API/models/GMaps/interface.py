from API import app
import json


class GMapsInterface():

    baseUrlDirection = "https://maps.googleapis.com/maps/api/directions/json?"
    baseUrlElevation = "https://maps.googleapis.com/maps/api/elevation/json?"

    def __init__(self):
        with open(app.config['PARENT_DIR'] + '/API/config/configMaps.json') as data_file:
            data = json.load(data_file)
            self.validUrlDirection = self.baseUrlDirection + "key=" + data["API_key"]
            self.validUrlElevation = self.baseUrlElevation + "key=" + data["API_key"]
