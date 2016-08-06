#!/usr/bin/env python
import os
import sys
from argparse import ArgumentParser

import yaml
from rtmbot import RtmBot


# def parse_args():
#     parser = ArgumentParser()
#     parser.add_argument(
#         '-c',
#         '--config',
#         help='Full path to config file.',
#         metavar='path'
#     )
#     return parser.parse_args()

# load args with config path
# args = parse_args()
# config = yaml.load(open(args.config or 'rtmbot.conf', 'r'))
config = {
    'SLACK_TOKEN': os.environ.get('SLACK_TOKEN'),
    'DEBUG': os.environ.get('DEBUG', True),
}
bot = RtmBot(config)
bot.start()
# try:
    # bot.start()
# except KeyboardInterrupt:
    # sys.exit(0)
