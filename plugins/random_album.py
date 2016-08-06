from __future__ import unicode_literals
# don't convert to ascii in py2.7 when creating string to return
import requests
import os

timeout = int(os.environ.get('SLACK_AOTD_TIMEOUT', 60 * 60 * 24))

crontable = []
outputs = []
crontable.append([timeout, "produce_album_of_the_day"])

message = "Today's album of the day from the Doomlist is..."
error_message = "Odd... Something went wrong."
url = "https://doomlist.herokuapp.com/slack/random"
data = {'token': os.environ.get('SLACK_APP_TOKEN')} 
channel = "C0A26H7PX"


def produce_album_of_the_day():
    outputs.append([channel, message])
    response = requests.post(url, data=data)
    if not response.ok or response.content == '':
        outputs.append([channel, error_message])
    else:
        response = response.json()
        response['channel'] = channel
        outputs.append([channel, response])