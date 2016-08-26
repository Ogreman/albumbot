from __future__ import unicode_literals
# don't convert to ascii in py2.7 when creating string to return
import requests
import os

time_of_job = str(os.environ.get('SLACK_CHECK_TIME', '04:51'))

crontable = []
outputs = []
timejobs = []
timejobs.append([time_of_job, "check_links"])

message = "I'm going to check every bandcamp URL in the Doomlist."
url = "https://doomlist.herokuapp.com/slack/check"
data = {'token': os.environ.get('SLACK_APP_TOKEN'), 'user_id': "U1YUJELR3", 'silence': "True"} 
channel = "C0A26H7PX"


def check_links():
    outputs.append([channel, message])
    response = requests.post(url, data=data)
    if not response.ok or response.content == '':
        outputs.append([channel, "Odd... Something went wrong."])