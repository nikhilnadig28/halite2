import hlt
import numpy as np
from collections import OrderedDict
from .Common import *



class ShipFeatures:
    def __init__(self, game_map, map_features, ship):
        self.game_map = game_map
        self.map_features = map_features
        self.ship = ship
        self.nearby_entities = np.array()
        self.values = np.array()

    #### Ship related functions ####

    # Get details of nearby planets in map
    def get_empty_planet_distances(self):
        empty_planet_distances = [distance for distance in self.nearby_entities
                                  if isinstance(self.nearby_entities[distance][0], hlt.entity.Planet)
                                  and not self.nearby_entities[distance][0].is_owned()]
        empty_planet_distances = pad_distances(empty_planet_distances)
        return empty_planet_distances[:MAX_SENSE_LIMIT]

    def get_team_planet_distances(self):
        team_planet_distances = [distance for distance in self.nearby_entities
                                 if isinstance(self.nearby_entities[distance][0], hlt.entity.Planet)
                                 and self.nearby_entities[distance][0].is_owned()
                                 and (self.nearby_entities[distance][0].owner.id == self.game_map.get_me().id)]
        team_planet_distances = pad_distances(team_planet_distances)
        return team_planet_distances[:MAX_SENSE_LIMIT]

    def get_enemy_planet_distances(self):
        enemy_planet_distances = [distance for distance in self.nearby_entities
                                  if isinstance(self.nearby_entities[distance][0], hlt.entity.Planet)
                                  and not self.nearby_entities[distance][0].is_owned()]
        enemy_planet_distances = pad_distances(enemy_planet_distances)
        return enemy_planet_distances[:MAX_SENSE_LIMIT]

    # Get details of nearby ships in map
    def get_team_ship_distances(self):
        team_ship_distances = [distance for distance in self.nearby_entities
                               if isinstance(self.nearby_entities[distance][0], hlt.entity.Planet)
                               and self.nearby_entities[distance][0].is_owned()
                               and (self.nearby_entities[distance][0].owner.id == self.game_map.get_me().id)]
        team_ship_distances = pad_distances(team_ship_distances)
        return team_ship_distances[:MAX_SENSE_LIMIT]

    def get_enemy_ship_distances(self):
        enemy_ship_distances = [distance for distance in self.nearby_entities
                                if isinstance(self.nearby_entities[distance][0], hlt.entity.Planet)
                                and not self.nearby_entities[distance][0].is_owned()]
        enemy_ship_distances = pad_distances(enemy_ship_distances)
        return enemy_ship_distances[:MAX_SENSE_LIMIT]

    def update_values(self):
        self.nearby_entities = self.game_map.nearby_nearby_entities()
        self.nearby_entities = OrderedDict(sorted(self.nearby_entities.items(), key=lambda t: t[0]))

        self.values = np.array(self.get_empty_planet_distances(),
                               self.get_team_planet_distances(),
                               self.get_enemy_planet_distances(),
                               self.get_team_ship_distances(),
                               self.get_enemy_ship_distances())
