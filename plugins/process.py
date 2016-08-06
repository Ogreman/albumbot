from __future__ import unicode_literals
# don't convert to ascii in py2.7 when creating string to return
import json
import requests
import os

timeout = int(os.environ.get('SLACK_PROCESS_TIMEOUT', 21600))

crontable = []
outputs = []
crontable.append([timeout, "process_albums"])

message = "I'm going to make sure any new albums have been processed in the Doomlist."
url = "https://doomlist.herokuapp.com/slack/process"
data = {'token': os.environ.get('SLACK_APP_TOKEN'), 'user_id': "U1YUJELR3"}


def process_albums():
    outputs.append(["C0A1YLG3X", message])
    response = requests.post(url, data=json.dumps(data))
    if not response.ok:
        outputs.append(["C0A1YLG3X", "Odd... Something went wrong."])