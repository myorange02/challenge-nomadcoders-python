# BLUEPRINT | DONT EDIT

import requests

movie_ids = [
    238, 680, 550, 185, 641, 515042, 152532, 120467, 872585, 906126, 840430
]

# /BLUEPRINT

# 👇🏻 YOUR CODE 👇🏻:

for id in movie_ids:
    url = f'https://nomad-movies.nomadcoders.workers.dev/movies/{id}'
    response = requests.get(url).json()
    print(f'Title: {response["title"]}\
          \nOverview: {response["overview"]}\
          \nAvg Vote: {response["vote_average"]}\n\n')

# /YOUR CODE