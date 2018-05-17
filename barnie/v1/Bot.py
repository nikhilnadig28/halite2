import hlt
import logging
import os
import numpy as np
from scipy import stats
from .GameState import GameState
from .ShipState import ShipState
from .NeuralNet import NeuralNetwork
from .Strategy import *

VERSION = 1

game = hlt.Game("barnie")
# Then we print our start message to the logs
logging.info("Starting Barnie!")


class Bot:
    def _init_(self, name):
        current_directory = os.path.dirname(os.path.abspath(__file__))
        self._name = name

        # Neural Network
        self.nn_layer = np.array(NUM_INPUTS, 10, NUM_OUTPUTS)
        self.nn = NeuralNetwork(self.nn_layer)

        # Game related
        self.game_map = game.update_map()

    def play(self):
        while True:
            self.game_map = game.update_map()
            commands = []
            game_state = GameState(self.game_map)

            for ship in self.game_map.get_me().all_ships():
                if ship.docking_status is not ship.DockingStatus.UNDOCKED:
                    continue

                ship_state = ShipState(self.game_map, game_state, ship)
                nn_input = np.append(game_state.values, ship_state.values)
                nn_out = self.nn.forward(nn_input)

                # Obtain an action
                #possible_actions = np.arange(3)
                #probabilities = stats.rv_discrete(name='custom', values=(possible_actions, nn_out))
                #action = probabilities.rvs(size=1)

                action = np.argmax(nn_out)

                commands.append(self.ship_command(ship, ship_state, action))

                game.send_command_queue(commands)

                with open("input.vec".format(VERSION), "a") as f:
                    f.write(str([round(item, 3) for item in nn_input]))
                    f.write('\n')

                with open("c{}_out.vec".format(VERSION), "a") as f:
                    f.write(str(nn_out))
                    f.write('\n')

    def ship_command(self, ship, ship_state, action):
        new_command = []
        if action is 0:
            '''Attack closest enemy ship'''
            target = ship_state.get_closest_enemy_ship()
            new_command = ship.navigate(
                ship.closest_point_to(target),
                self.game_map, speed=int(hlt.constants.MAX_SPEED), ignore_ships=False)

        elif action is 1:
            '''Dock and mine closest owned/neutral planet'''
            target = ship_state.get_closest_available_planet()
            if target.isFull():
                # Go attack if the planet is full
                self.ship_command(ship, ship_state, 0)
            else:
                if ship.can_dock(target):
                    new_command = ship.dock(target)
                else:
                    new_command = ship.navigate(
                        ship.closest_point_to(target),
                        self.game_map, speed=int(hlt.constants.MAX_SPEED), ignore_ships=False)

        elif action is 2:
            pass

        return new_command
