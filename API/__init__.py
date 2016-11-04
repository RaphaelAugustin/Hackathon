import os
from flask import Flask


app = Flask(__name__)

from API.routes import main
from API.routes import GMaps
