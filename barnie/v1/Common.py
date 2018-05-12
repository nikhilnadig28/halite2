import numpy as np
from .Strategy import *


def pad_distances(distances):
    if len(distances) < MAX_SENSE_LIMIT:
        num_pads = MAX_SENSE_LIMIT - len(distances)
        distances.extend(np.full(num_pads, -99))
    return distances
