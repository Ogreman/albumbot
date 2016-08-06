from __future__ import unicode_literals
# don't convert to ascii in py2.7 when creating string to return

import requests

crontable = []
outputs = []

message = "There are {} albums in the Doomlist."
url = "https://doomlist.herokuapp.com/api/albums/count"


def process_message(data):
    if 'text' in data:
        contents = data['text'].lower()
        if 'how many' in contents and 'doomlist' in contents:
            response = requests.get(url)
            if response.ok:
                try:
                    count = response.json().get('count')
                except KeyError:
                    pass
                else:
                    outputs.append(
                        [data['channel'], message.format(count)]
                    )
