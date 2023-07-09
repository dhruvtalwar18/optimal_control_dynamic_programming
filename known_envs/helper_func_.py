from utils import *
# final_path = "./envs/known_envs/doorkey-6x6-normal.env"
import itertools
import numpy as np
from path_names_ import final_path

env, info = load_env(final_path)
agent_dir2 = env.agent_dir

goal = info["goal_pos"]
key = info["key_pos"]
door = info["door_pos"]

def get_obstacles(pos):
    obstacles = []
    for i in range(env.height):
        for j in range(env.width):
            element = env.grid.get(j, i)
            if element is not None and element.type == "wall":
                obstacles.append([j, i])
    if pos in obstacles:
        return True
    else:
        return False
def obstacles_list():
    env, info = load_env(final_path)
    obstacles = []
    for i in range(env.height):
        for j in range(env.width):
            element = env.grid.get(j, i)
            if element is not None and element.type == "wall":
                obstacles.append([j, i])
    return obstacles

def new_states():
    obstacles = obstacles_list()
    obstacles = np.array(obstacles)
    x_coords = np.arange(0, env.width)
    y_coords = np.arange(0, env.height)
    orient = np.arange(0, 4)
    door_vals = np.array([0, 1])
    key_vals = np.array([0, 1])
    state_space_nowalls = np.array(list(itertools.product(x_coords, y_coords, orient, key_vals, door_vals)))
    remove_indices = np.logical_or.reduce([np.logical_and(state_space_nowalls[:, 0] == obs[0],state_space_nowalls[:, 1] == obs[1])for obs in obstacles])
    state_space1 = state_space_nowalls[~remove_indices]
    return state_space1

def dict_array():
    state_spaces = new_states()
    state_dict = {}
    for i in range(len(state_spaces)):
        state_dict[tuple(state_spaces[i])] = i
    return state_dict