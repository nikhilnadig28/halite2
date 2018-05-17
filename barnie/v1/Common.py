import numpy as np
from .Strategy import *


def pad_distances(distances):
    if len(distances) < MAX_SENSE_LIMIT:
        num_pads = MAX_SENSE_LIMIT - len(distances)
        distances.extend(np.full(num_pads, -99))
    return distances

def normalize(array):
    max_value = np.max(np.abs(array))
    if max_value is not 0:
        return np.divide(array/max_value)
    else
        return