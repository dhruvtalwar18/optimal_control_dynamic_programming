import numpy as np
from utils import *

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
def motion_model1(state, action):
    motion_output = state.copy()
    temp_state = [0, 0, 0, 0, 0]
    temp_state = orientation_matcher(state)
    if action == "MF":

        if get_obstacles([temp_state[0], temp_state[1]]):
            motion_output = state

        elif temp_state[0] == door[0] and temp_state[1] == door[1] and state[4] == 0:
            motion_output = state

        elif temp_state[0] == door[0] and temp_state[1] == door[1] and state[4] == 1:
            motion_output = temp_state

        elif temp_state[0] == key[0] and temp_state[1] == key[1] and state[3] == 0:
            motion_output = state

        elif temp_state[0] == key[0] and temp_state[1] == key[1] and state[3] == 1:
            motion_output = temp_state

        else:
            motion_output = temp_state

    elif action == "TL":
        motion_output[2] = (state[2] - 1) % 4
        motion_output = motion_output

    elif action == "TR":
        motion_output[2] = (state[2] + 1) % 4
        motion_output = motion_output

    elif action == "UD":
        if temp_state[0] == door[0] and temp_state[1] == door[1] and state[3] == 1:
            motion_output[4] = 1
            motion_output = motion_output

        else:
            motion_output[4] = 0
            motion_output = motion_output


    elif action == "PK":
        if temp_state[0] == key[0] and temp_state[1] == key[1] and state[3] == 0:
            motion_output[3] = 1

            motion_output = motion_output
        else:
            motion_output = motion_output
    else:
        motion_output = motion_output
    return motion_output


def orientation_matcher(state, temp_state=[0, 0, 0, 0, 0]):
    if state[2] == 0:
        temp_state[0] = min(state[0] + 1, env.height - 1)
        temp_state[1] = state[1]
        temp_state[2] = state[2]
        temp_state[3] = state[3]
        temp_state[4] = state[4]

    if state[2] == 1:
        temp_state[0] = state[0]
        temp_state[1] = min(state[1] + 1, env.width - 1)
        temp_state[2] = state[2]
        temp_state[3] = state[3]
        temp_state[4] = state[4]

    if state[2] == 2:
        temp_state[0] = max(state[0] - 1, 0)
        temp_state[1] = state[1]
        temp_state[2] = state[2]
        temp_state[3] = state[3]
        temp_state[4] = state[4]

    if state[2] == 3:
        temp_state[0] = state[0]
        temp_state[1] = max(state[1] - 1, 0)
        temp_state[2] = state[2]
        temp_state[3] = state[3]
        temp_state[4] = state[4]

    return temp_state
