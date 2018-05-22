# Add the b directory to your sys.path

import hlt
import logging
import sys
import os
from Bot import Bot
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-name', action="store", dest='name', default='0')
args = parser.parse_args()

myBot = Bot(str(args.name))
myBot.play()


