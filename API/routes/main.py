from API import app
from API.controllers import main


app.add_url_rule(
    '/get/<int:pokeId>/',
    'get',
    main.get,
    methods=["GET"]
)
