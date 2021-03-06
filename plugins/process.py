from __future__ import unicode_literals
# don't convert to ascii in py2.7 when creating string to return
import requests
import os

time_of_job = str(os.environ.get('SLACK_CHECK_TIME', '16:00'))
weekday = 2

crontable = []
outputs = []
timejobs = []
weeklyjobs = []
weeklyjobs.append([(time_of_job, weekday), "process_albums"])

message = "I'm going to make sure any new albums have been processed in the Doomlist."
url = "https://doomlist.herokuapp.com/slack/process"
data = {'token': os.environ.get('SLACK_APP_TOKEN'), 'user_id': "U1YUJELR3", 'silence': "True"} 
channel = "C0A26H7PX"


def process_albums():
    outputs.append([channel, message])
    response = requests.post(url, data=data)
    if not response.ok or response.content == '':
        outputs.append([channel, "Odd... Something went wrong."])