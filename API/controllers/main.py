import os
from flask import request
from json import dumps
from random import choice

from API import app


def get():
    cities = ['Baghdad', 'Hanoi', 'Los Angeles', 'Alexandria', 'Durban', 'Jakarta', 'Kinshasa', 'Dhaka', 'Kolkata', 'Riyadh', 'Seoul', 'Yokohama', 'Shenzhen', 'Yangon', 'Surat', 'New York City', 'Berlin', 'Ouagadougou']

    if (
        "weight" in request.form
        and "start" in request.form
        and "end" in request.form
        and "pokemonId" in request.form
    ):
        stage1 = choice(cities)

        stage2 = choice(cities)
        while stage2 == stage1:
            stage2 = choice(cities)

        stage3 = choice(cities)
        while stage3 == stage1 or stage3 == stage2:
            stage3 = choice(cities)

        # Point de départ : request.form['start']
        # Etape 1, 2 et 3 : stage1, stage2, stage3
        # Destination : request.form['end']

        return dumps({"success": True})

    else:
        return dumps({
            "success": False,
            "message": "Missing parameters"
        }, indent=4)
