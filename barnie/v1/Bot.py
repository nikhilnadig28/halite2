import hlt
import logging
import os
import numpy as np

game = hlt.Game("barnie")
# Then we print our start message to the logs
logging.info("Starting Barnie!")

class Bot:
    def _init_(self, name):
        current_directory = os.path.dirname(os.path.abspath(__file__))
        self._name = name


    def play(self):
        while True:
            game_map = game.update_map()
            commands = []

            # Get all features here
            # Pass them to the neural network
            # Get outputs
