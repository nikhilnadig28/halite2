import math

# number of features to track
HM_ENT_FEATURES = 3

# Max number of planets.
PLANET_MAX_NUM = 28

# These are the features we compute per planet
FEATURE_NAMES = [
    "health",
    "available_docking_spots",
    "remaining_production",
    "signed_current_production",
    "gravity",
    "closest_friendly_ship_distance",
    "closest_enemy_ship_distance",
    "ownership",
    "distance_from_center",
    "weighted_average_distance_from_friendly_ships",
    "is_active"]

# Number of initial features per planet we have
PER_PLANET_FEATURES = len(FEATURE_NAMES)

def distance2(x1, y1, x2, y2):
    return (x1 - x2) ** 2 + (y1 - y2) ** 2


def distance(x1, y1, x2, y2):
    return math.sqrt(distance2(x1, y1, x2, y2))


def key_by_value(dictionary, value):
    for k, v in dictionary.items():
        if v[0] == value:
            return k
    return -99


def fix_data(data):
    new_list = []
    last_known_idx = 0
    for i in range(HM_ENT_FEATURES):
        try:
            if i < len(data):
                last_known_idx = i
            new_list.append(data[last_known_idx])
        except:
            new_list.append(0)

    return new_list