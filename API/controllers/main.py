import os
from flask import request
from json import dumps

from API import app


def get(pokeId):
    return dumps({"pokemon number": pokeId})
