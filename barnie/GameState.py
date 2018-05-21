import hlt
import logging
import numpy as np


class GameState:
    def __init__(self, game_map):
        self.game_map = game_map
        self.values = np.array([])
        self.update_values()

    #### Map related functions ###
    def get_friendly_ships_count(self):
        return len(self.game_map.get_me().all_ships())

    def get_all_ships_count(self):
        return len(self.game_map._all_ships())

    def get_enemy_ships_count(self):
        #return len([ship for ship in self.game_map.all_ships() if ship not in self.get_friendly_ships()])
        return self.get_all_ships_count()-self.get_friendly_ships_count()

    def get_num_teams(self):
        pass

    def update_values(self):
        logging.info('Number of enemy ships' + str(self.get_enemy_ships_count()))
        logging.info('Number of friendly ships' + str(self.get_enemy_ships_count()))
        self.values = np.array([self.get_friendly_ships_count(),
                               self.get_enemy_ships_count()])





