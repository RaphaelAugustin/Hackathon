import os
from flask import Flask

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.dirname(CURRENT_DIR)

app = Flask(__name__)

app.config['PARENT_DIR'] = PARENT_DIR

from API.routes import main
from API.routes import GMaps
