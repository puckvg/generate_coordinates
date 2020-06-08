#!/usr/bin/env python3
from sphere_point_picking import sample_sphere_cartesian
import numpy as np

def get_coordinates(central_coordinates, mu, sigma): 
    r = np.random.normal(mu, sigma) 
    vector = sample_sphere_cartesian(r)
    new_coords = vector + central_coordinates
    return new_coords
