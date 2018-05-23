# Add the b directory to your sys.path

import hlt
import logging
import sys
import os
import v1
import numpy as np
from v1.Bot import Bot
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('-name', action="store", dest='name', default='0')
parser.add_argument('-w', '--weights', nargs='+', type=float, dest='weights', help='<Required> Set flag', default=None)
args = parser.parse_args()

if args.weights:
    myBot = Bot(str(args.name), np.array(args.weights))
    myBot.play()
else:
    myBot = Bot(str(args.name))
    myBot.play()



