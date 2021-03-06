import hlt
import logging
import numpy as np
from collections import OrderedDict
from v1.Common import *



class ShipState:
    def __init__(self, game_map, game_features, ship):
        self.game_map = game_map
        self.map_features = game_features
        self.ship = ship
        self.team_id = self.game_map.get_me().id
        self.nearby_entities = self.game_map.nearby_entities_by_distance(ship)
        self.nearby_entities = OrderedDict(sorted(self.nearby_entities.items(), key=lambda t: t[0]))
        self.values = np.zeros(5)
        self.update_values()

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
                                 and (self.nearby_entities[distance][0].owner.id == self.team_id)]
        team_planet_distances = pad_distances(team_planet_distances)
        return team_planet_distances[:MAX_SENSE_LIMIT]

    def get_enemy_planet_distances(self):
        enemy_planet_distances = [distance for distance in self.nearby_entities
                                  if isinstance(self.nearby_entities[distance][0], hlt.entity.Planet)
                                  and self.nearby_entities[distance][0].is_owned()
                                  and not (self.nearby_entities[distance][0].owner.id == self.team_id)]
        enemy_planet_distances = pad_distances(enemy_planet_distances)
        return enemy_planet_distances[:MAX_SENSE_LIMIT]

    # Get details of nearby ships in map
    def get_team_ship_distances(self):
        team_ship_distances = [distance for distance in self.nearby_entities
                               if isinstance(self.nearby_entities[distance][0], hlt.entity.Ship)
                               and (self.nearby_entities[distance][0].owner.id == self.team_id)]
        team_ship_distances = pad_distances(team_ship_distances)
        return team_ship_distances[:MAX_SENSE_LIMIT]

    def get_enemy_ship_distances(self):
        enemy_ship_distances = [distance for distance in self.nearby_entities
                                if isinstance(self.nearby_entities[distance][0], hlt.entity.Ship)
                                and not (self.nearby_entities[distance][0].owner.id == self.team_id)]
        enemy_ship_distances = pad_distances(enemy_ship_distances)
        return enemy_ship_distances[:MAX_SENSE_LIMIT]

    def get_closest_enemy_ship(self):
        min_dist = 99999
        closest_enemy_ship = None
        for distance in self.nearby_entities:
            entity = self.nearby_entities[distance][0]
            if isinstance(entity, hlt.entity.Ship):
                if entity.owner.id is not self.team_id:
                    if min_dist > distance:
                        closest_enemy_ship = entity
                        min_dist = distance
        return closest_enemy_ship

    def get_closest_available_planet(self):
        min_dist = 99999
        closest_available_planet = None
        for distance in self.nearby_entities:
            entity = self.nearby_entities[distance][0]
            if isinstance(entity, hlt.entity.Planet):
                if entity.is_owned() and not entity.is_full():
                    if entity.owner.id is self.team_id:
                        if min_dist > distance:
                            closest_available_planet = entity
                            min_dist = distance
                else:
                    if min_dist > distance:
                        closest_available_planet = entity
                        min_dist = distance
        return closest_available_planet

    def update_values(self):
        self.values = np.array([self.get_empty_planet_distances(),
                               self.get_team_planet_distances(),
                               self.get_enemy_planet_distances(),
                               self.get_team_ship_distances(),
                               self.get_enemy_ship_distances()])
