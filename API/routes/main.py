from API import app
from API.controllers import main


app.add_url_rule(
    '/get',
    'get',
    main.get,
    methods=["POST"]
)
