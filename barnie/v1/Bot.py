import hlt
import logging
import os
import numpy as np
from scipy import stats
from .GameState import GameState
from .ShipState import ShipState
from .NeuralNet import Neural_Network
from .Strategy import *

game = hlt.Game("barnie")
# Then we print our start message to the logs
logging.info("Starting Barnie!")

class Bot:
    def _init_(self, name):
        current_directory = os.path.dirname(os.path.abspath(__file__))
        self._name = name

        # Neural Network
        self.nn_layer = np.array(NUM_INPUTS, 10, 10, NUM_OUTPUTS)
        self.nn = Neural_Network(self.nn_layer)

        # Game related
        self.game_map = game.update_map()


    def play(self):
        while True:
            self.game_map = game.update_map()
            commands = []

            game_features = GameState(game_map)
            nn_input = game_features.values

            for ship in game_map.get_me().all_ships():
                if ship.docking_status is not ship.DockingStatus.UNDOCKED:
                    continue

                ship_features = ShipState(game_map, game_features, ship)
                nn_input = np.append(game_features.values, ship_features.values)
                nn_out = self.nn.forward(nn_input)

                # Obtain an action
                possible_actions = np.arange(3)
                probabilities = stats.rv_discrete(name='custm', values=(possible_actions, prob1))
                action = probabilities.rvs(size=1)

                commands.append(self.ship_command(ship, action))

    def ship_command(self, ship, action):
        if action is 0:
            new_command = ship.navigate(
                ship.closest_point_to(closest_enemy_ships[0]), self.game_map, speed=int(hlt.constants.MAX_SPEED),
                ignore_ships=False)

