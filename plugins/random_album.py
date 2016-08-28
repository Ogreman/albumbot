from __future__ import unicode_literals
# don't convert to ascii in py2.7 when creating string to return
import requests
import os

# timeout = int(os.environ.get('SLACK_AOTD_TIMEOUT', 60 * 60 * 24))
time_of_job = str(os.environ.get('SLACK_AOTD_TIME', '10:00'))

crontable = []
outputs = []
timejobs = []
# crontable.append([timeout, "produce_album_of_the_day"])
timejobs.append([time_of_job, "produce_album_of_the_day"])


message = "Today's album of the day from the Doomlist is: {url}"
error_message = "Odd... Something went wrong."
url = "https://doomlist.herokuapp.com/slack/random"
data = {'token': os.environ.get('SLACK_APP_TOKEN')} 
channel = "C0A8M8B9Q" # announcements


def produce_album_of_the_day():
    response = requests.post(url, data=data)
    if not response.ok or response.content == '':
        outputs.append([channel, error_message])
    else:
        response = response.json()
        response['channel'] = channel
        response['text'] = message.format(url=response['text'])
        outputs.append([channel, response])