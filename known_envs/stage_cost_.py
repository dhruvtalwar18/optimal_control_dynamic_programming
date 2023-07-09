import numpy as np
from utils import *
from helper_func_ import get_obstacles
from path_names_ import final_path


env, info = load_env(final_path)
agent_dir2 = env.agent_dir
goal = info["goal_pos"]

key = info["key_pos"]
door = info["door_pos"]


def stage_cost(state, action):

    if action == "MF":
        state_temp = state.copy()
        if state[2] == 0:
            state_temp[0] = min(state_temp[0] + 1, env.height - 1)
        if state[2] == 1:
            state_temp[1] = min(state_temp[1] + 1, env.width - 1)
        if state[2] == 2:
            state_temp[0] = max(state_temp[0] - 1, 0)
        if state[2] == 3:
            state_temp[1] = max(state_temp[1] - 1, 0)
        if get_obstacles([state_temp[0], state_temp[1]]):
            return np.inf
        if state_temp[0] == goal[0] and state_temp[1] == goal[1]:
            return 10
        if state_temp[0] == door[0] and state_temp[1] == door[1] and state_temp[4] == 1:
            return 10
        if state_temp[0] == door[0] and state_temp[1] == door[1] and state_temp[4] == 0:
            return np.inf
        if state_temp[0] == key[0] and state_temp[1] == key[1] and state_temp[3] == 0:
            return np.inf

        else:
            return 10


    elif action == "TL" or action == "TR":
        return 10

    elif action == "PK":
        state_temp = state.copy()
        if state[2] == 0:
            state_temp[0] = min(state_temp[0] + 1, env.height - 1)

        if state[2] == 1:
            state_temp[1] = min(state_temp[1] + 1, env.width - 1)

        if state[2] == 2:
            state_temp[0] = max(state_temp[0] - 1, 0)

        if state[2] == 3:
            state_temp[1] = max(state_temp[1] - 1, 0)

        if get_obstacles([state_temp[0], state_temp[1]]):
            return np.inf

        if state_temp[0] == key[0] and state_temp[1] == key[1] and state_temp[3] == 0 and state_temp[4] == 0:
            return 10

        if state_temp[0] == key[0] and state_temp[1] == key[1] and state_temp[3] == 0 and state_temp[4] == 1:
            return np.inf


        if state_temp[0] == key[0] and state_temp[1] == key[1] and state_temp[3] == 1 and state_temp[4] == 0:
            return np.inf

        if state_temp[0] == key[0] and state_temp[1] == key[1] and state_temp[3] == 1 and state_temp[4] == 1:
            return np.inf


        if state_temp[0] != key[0] and state_temp[1] != key[1]:
            return np.inf


        else:
            return 10

    elif action == "UD":
        state_temp = state.copy()
        if state[2] == 0:
            state_temp[0] = min(state_temp[0] + 1, env.height - 1)

        if state[2] == 1:
            state_temp[1] = min(state_temp[1] + 1, env.width - 1)

        if state[2] == 2:
            state_temp[0] = max(state_temp[0] - 1, 0)

        if state[2] == 3:
            state_temp[1] = max(state_temp[1] - 1, 0)

        if get_obstacles([state_temp[0], state_temp[1]]):
            return np.inf


        if state_temp[0] == door[0] and state_temp[1] == door[1] and state_temp[4] == 1 and state_temp[3] == 0:
            return np.inf

        if state_temp[0] == door[0] and state_temp[1] == door[1] and state_temp[4] == 1 and state_temp[3] == 1:
            return np.inf

        if state_temp[0] == door[0] and state_temp[1] == door[1] and state_temp[4] == 0 and state_temp[3] == 0:
            return np.inf

        if state_temp[0] == door[0] and state_temp[1] == door[1] and state_temp[4] == 0 and state_temp[3] == 1:
            return 10

        if state_temp[0] != door[0] and state_temp[1] != door[1]:
            return np.inf

        else:
            return 10

