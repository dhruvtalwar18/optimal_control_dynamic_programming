import numpy as np
import os
from itertools import product
import itertools
from utils import *
from tqdm import tqdm

##################################################################
door_2 = [4,5]
door_1 = [4,2]

env_folder = "./envs/random_envs"
env, info, env_path = load_random_env(env_folder)

name_file = env_path.split("/")[-1].split(".")[0]
actions = ["MF", "TL", "TR", "PK", "UD"]


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
    door1 = np.array([0, 1])
    door2 = np.array([0, 1])
    key_stat = np.array([0, 1])
    key_pos = np.arange(0,3)
    goal_pos = np.arange(0,3)
    state_space_nowalls = np.array(list(itertools.product(x_coords, y_coords, orient, door1,door2, key_stat,key_pos,goal_pos)))
    remove_indices = np.logical_or.reduce([np.logical_and(state_space_nowalls[:, 0] == obs[0],state_space_nowalls[:, 1] == obs[1])for obs in obstacles])
    state_space1 = state_space_nowalls[~remove_indices]
    return state_space1

def dict_array():
    state_spaces = new_states()
    state_dict = {}
    for i in range(len(state_spaces)):
        state_dict[tuple(state_spaces[i])] = i
    return state_dict

key_possible = {0:[1,1], 1:[2,3], 2:[1,6]}
goal_possible = {0:[5,1], 1:[6,3], 2:[5,6]}

def orientation_matcher(state, temp_state=[0,0,0,0,0,0,0,0]):
    if state[2] == 0:
        temp_state[0] = min(state[0] + 1, env.height - 1)
        temp_state[1] = state[1]
        temp_state[2] = state[2]
        temp_state[3] = state[3]
        temp_state[4] = state[4]
        temp_state[5] = state[5]
        temp_state[6] = state[6]
        temp_state[7] = state[7]


    if state[2] == 1:
        temp_state[0] = state[0]
        temp_state[1] = min(state[1] + 1, env.width - 1)
        temp_state[2] = state[2]
        temp_state[3] = state[3]
        temp_state[4] = state[4]
        temp_state[5] = state[5]
        temp_state[6] = state[6]
        temp_state[7] = state[7]


    if state[2] == 2:
        temp_state[0] = max(state[0] - 1, 0)
        temp_state[1] = state[1]
        temp_state[2] = state[2]
        temp_state[3] = state[3]
        temp_state[4] = state[4]
        temp_state[5] = state[5]
        temp_state[6] = state[6]
        temp_state[7] = state[7]

    if state[2] == 3:
        temp_state[0] = state[0]
        temp_state[1] = max(state[1] - 1, 0)
        temp_state[2] = state[2]
        temp_state[3] = state[3]
        temp_state[4] = state[4]
        temp_state[5] = state[5]
        temp_state[6] = state[6]
        temp_state[7] = state[7]


    return temp_state

def motion_model1(state, action):
    motion_output = state.copy()
    temp_state = [0,0,0,0,0,0,0,0]
    temp_state = orientation_matcher(state)
    if action == "MF":

        if get_obstacles([temp_state[0], temp_state[1]]):
            motion_output = state

        elif temp_state[0] == door_1[0] and temp_state[1] == door_1[1] and state[3] == 0:
            motion_output = state

        elif temp_state[0] == door_1[0] and temp_state[1] == door_1[1] and state[3] == 1:
            motion_output = temp_state
        ####################################DOOR 2#############################################
        elif temp_state[0] == door_2[0] and temp_state[1] == door_2[1] and state[4] == 0:
            motion_output = state

        elif temp_state[0] == door_2[0] and temp_state[1] == door_2[1] and state[4] == 1:
            motion_output = temp_state

        elif temp_state[0] == key_possible[state[6]][0] and temp_state[1] == key_possible[state[6]][1] and state[5] == 0:
            motion_output = state

        elif temp_state[0] == key_possible[state[6]][0] and temp_state[1] == key_possible[state[6]][0] and state[5] == 1:
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
        if temp_state[0] == door_1[0] and temp_state[1] == door_1[1] and state[5] == 1:
            motion_output[3] = 1
            motion_output = motion_output
        if temp_state[0] == door_2[0] and temp_state[1] == door_2[1] and state[5] == 1:
            motion_output[4] = 1
            motion_output = motion_output

        else:
            motion_output = motion_output


    elif action == "PK":
        if temp_state[0] == key_possible[state[6]][0] and temp_state[1] == key_possible[state[6]][1] and state[5] == 0:
            motion_output[5] = 1

            motion_output = motion_output
        else:
            motion_output = motion_output
    else:
        motion_output = motion_output
    return motion_output

######################################################################################################

def stage_cost(state, action):
    goal = goal_possible[state[7]]
    key = key_possible[state[6]]

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
        if state_temp[0] == door_1[0] and state_temp[1] == door_1[1] and state_temp[3] == 1:
            return 10
        if state_temp[0] == door_1[0] and state_temp[1] == door_1[1] and state_temp[3] == 0:
            return np.inf

        if state_temp[0] == door_2[0] and state_temp[1] == door_2[1] and state_temp[4] == 1:
            return 10
        if state_temp[0] == door_2[0] and state_temp[1] == door_2[1] and state_temp[4] == 0:
            return np.inf
        if state_temp[0] == key[0] and state_temp[1] == key[1] and state_temp[5] == 0:
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

        if state_temp[0] == key[0] and state_temp[1] == key[1] and state_temp[5] == 0 and state_temp[3] == 0 and state_temp[4] == 0:
            return 10


        if state_temp[0] == key[0] and state_temp[1] == key[1] and state_temp[3] == 0 and state_temp[4] == 1:
            return 10
        if state_temp[0] == key[0] and state_temp[1] == key[1] and state_temp[3] == 1 and state_temp[4] == 0:
            return 10


        if state_temp[0] == key[0] and state_temp[1] == key[1] and state_temp[5] == 1:
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


        if state_temp[0] == door_1[0] and state_temp[1] == door_1[1] and state_temp[3] == 1 and state_temp[5] == 0:
            return np.inf

        if state_temp[0] == door_1[0] and state_temp[1] == door_1[1] and state_temp[3] == 1 and state_temp[5] == 1:
            return np.inf

        if state_temp[0] == door_1[0] and state_temp[1] == door_1[1] and state_temp[3] == 0 and state_temp[5] == 0:
            return np.inf

        if state_temp[0] == door_1[0] and state_temp[1] == door_1[1] and state_temp[3] == 0 and state_temp[5] == 1:
            return 10

        if state_temp[0] != door_1[0] and state_temp[1] != door_1[1]:
            return np.inf

        ######################################################################################
        if state_temp[0] == door_2[0] and state_temp[1] == door_2[1] and state_temp[4] == 1 and state_temp[5] == 0:
            return np.inf

        if state_temp[0] == door_2[0] and state_temp[1] == door_2[1] and state_temp[4] == 1 and state_temp[5] == 1:
            return np.inf

        if state_temp[0] == door_2[0] and state_temp[1] == door_2[1] and state_temp[4] == 0 and state_temp[5] == 0:
            return np.inf

        if state_temp[0] == door_2[0] and state_temp[1] == door_2[1] and state_temp[4] == 0 and state_temp[5] == 1:
            return 10

        if state_temp[0] != door_2[0] and state_temp[1] != door_2[1]:
            return np.inf

        else:
            return 10


state_space_final = new_states()
T_horizon = len(state_space_final)
print("The time horizon is:", T_horizon)
V = np.ones([T_horizon, len(state_space_final)]) * np.inf
P = -1 * np.ones([T_horizon, len(state_space_final)])
Q = np.ones((len(state_space_final), 5))
print("The shape of V is:", V.shape)
print("The shape of P is:", P.shape)
print("The shape of Q is:", Q.shape)
print("The shape of state_space_final is:", len(state_space_final))
#########################################################################################################################
# The following code is for the final state space
########################################################################################################################

def final():
    orientations = np.arange(4)
    d1_values = np.arange(2)
    d2_values = np.arange(2)
    k_values = np.arange(2)
    key_pos_values = np.arange(3)
    state_space_temp = new_states()
    for states in tqdm(state_space_temp):
        goal = goal_possible[states[7]]
        # key = key_possible[states[6]]
        for orientation, d1, d2, k, key_pos in product(orientations, d1_values, d2_values, k_values, key_pos_values):
            goal_state = np.array([goal[0], goal[1], orientation, d1, d2, k, key_pos, states[7]])
            mask = (state_space_temp == goal_state).all(axis=1)
            g_idx = np.where(mask)[0][0]
            V[T_horizon - 1, g_idx] = -1000
            Q[g_idx] = -1000

    state_space_1 = new_states()
    state_dict = dict_array()
    for i in tqdm(range(T_horizon - 2,-1, -1)):
        for states in state_space_1:
            goal = goal_possible[states[7]]

            # if state is goal state ignore that state
            if states[0] == goal[0] and states[1] == goal[1]:
                continue

            for action in range(len(actions)):
                index_old = state_dict[tuple(states)]
                stage_cost_ = stage_cost(states, actions[action])
                x_t_1 = tuple(motion_model1(states, actions[action]))
                index_new = state_dict[x_t_1]
                Q[index_old, action] = stage_cost_ + V[i + 1, index_new]

        V[i] = np.min(Q, axis=1)
        P[i] = np.argmin(Q, axis=1)

        print(i)
        t_start =i
        V[i] = np.min(Q, axis=1)
        P[i] = np.argmin(Q, axis=1)
        if np.array_equal(V[i], V[i + 1]):
            t_start = i
            print("Converged at time step", t_start)
            print(
                "#####################################################################################################")
            break

    return V, P, t_start

V, P, t_start1 = final()
t1 = t_start1

########################################################################################################################
dict_action = {0:"MF", 1:"TL", 2:"TR", 3:"PK", 4:"UD"}
mapping = dict_array()
########################################################################################################################
key_possible_reverse = {(1,1):0, (2,3):1,(1,6):2}
goal_possible_reverse = {(5,1):0,(6,3):1,(5,6):2}
########################################################################################################################
gg = tuple(info["goal_pos"])
kk = tuple(info["key_pos"])
k_stat = key_possible_reverse[kk]
g_stat = goal_possible_reverse[gg]
########################################################################################################################
door1 = env.grid.get(4, 2)
door2 = env.grid.get(4, 5)
if door1.is_open:
    d1_stat = 1
else:
    d1_stat = 0
if door2.is_open:
    d2_stat = 1
else:
    d2_stat = 0
state = [3,5,3,d1_stat,d2_stat,0,k_stat,g_stat]
print("Initial State",state)
goal = goal_possible[state[7]]
########################################################################################################################
action_final = []
copy = state.copy()
seq = []
state_space_final = new_states()
final_time = len(state_space_final)
print("The random map is", env_path)
########################################################################################################################
while t1< final_time:
    index = mapping[tuple(state)]
    action = P[t1, index]
    print("Action",action)
    seq.append(action)
    copy = state.copy()
    state = motion_model1(copy, str(dict_action[action]))
    t1 = t1 + 1
    action_final.append(dict_action[action])
    if state[0] == goal[0] and state[1] == goal[1]:
        break
seq.append(0)
print("Final Actions",action_final)
print("Final seq ",seq)
name = env_path.split("/")[-1].split("\\")[-1].split(".")[0]
#You can give the path before running the code
draw_gif_from_seq(seq, env,path="./gif/"+name+".gif")
#####################################################################################################

########################################################################################################################

