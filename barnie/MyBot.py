# Add the b directory to your sys.path

import hlt
import logging
import sys
import os
import v1
from v1.Bot import Bot
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('-name', action="store", dest='name', default='0')
# parser.add_argument('-w', action="store", dest='weights', default='0')
parser.add_argument('-w', '--weights', nargs='+', dest='weights', help='<Required> Set flag', default=None)
args = parser.parse_args()

if args.weights:
    myBot = Bot(str(args.name), args.weights)
    myBot.play()
else:
    myBot = Bot(str(args.name))
    myBot.play()



