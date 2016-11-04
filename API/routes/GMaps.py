from API import app
from API.controllers .GMaps import GMaps

app.add_url_rule(
    '/GMaps/getTraject/',
    'getTraject',
    GMaps.getTraject,
    methods=["POST"]
)
