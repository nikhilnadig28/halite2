import hlt
import logging
import numpy as np


class MapFeatures:
    def __init__(self, game_map):
        self.game_map = game_map
        self.values = np.array()
        self.update_values()

    #### Map related functions ###
    def get_friendly_ships_count(self):
        return self.game_map.get_me().all_ships()

    def get_all_ships_count(self):
        return self.game_map.all_ships()

    def get_enemy_ships(self):
        #return len([ship for ship in self.game_map.all_ships() if ship not in self.get_friendly_ships()])
        return self.get_all_ships_count()-self.get_friendly_ships_count()

    def get_num_teams(self):
        pass

    def update_values(self):
        #TODO





