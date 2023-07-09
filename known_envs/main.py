import numpy as np
from utils import *
from motion_model_ import motion_model1
from helper_func_ import new_states
from stage_cost_ import stage_cost
from helper_func_ import dict_array
from path_names_ import final_path

name_file = final_path.split("/")[-1].split(".")[0]
actions = ["MF", "TL", "TR", "PK", "UD"]
env, info = load_env(final_path)
agent_dir2 = env.agent_dir
goal = info["goal_pos"]
key = info["key_pos"]
door = info["door_pos"]
start = env.agent_pos

print("######################################################################################################################")
print(start, "start position")
print(goal, "goal position coordinates")
state_space_final = new_states()
T_horizon = len(state_space_final)
print("The time horizon is:", T_horizon)
V = np.ones([T_horizon,len(state_space_final)]) * np.inf
P = -1 * np.ones([T_horizon,len(state_space_final)])
Q = np.ones((len(state_space_final), 5))
print("######################################################################################################################")

def main_dynamic_algo():
    state_spaces1 = new_states()
    for orientation in range(4):
        for door_status in range(2):
            for key_status in range(2):
                goal_state = np.array([goal[0], goal[1], orientation, key_status, door_status])
                mask = (state_spaces1 == goal_state).all(axis=1)
                g_idx = np.where(mask)[0][0]
                V[T_horizon-1, g_idx] = -1000
                Q[g_idx] = -1000

    state_dict = dict_array()
    for i in range(T_horizon-2, -1, -1):
        for states in state_spaces1:
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

        #print(i)
        V[i] = np.min(Q, axis=1)
        P[i] = np.argmin(Q, axis=1)
        if np.array_equal(V[i], V[i + 1]):
            t_start = i
            print("Converged at time step",t_start)
            print("#####################################################################################################")
            break


    return V, P, t_start

v,p, t = main_dynamic_algo()
dict_action = {0:"MF", 1:"TL", 2:"TR", 3:"PK", 4:"UD"}
mapping = dict_array()

state = [start[0],start[1],agent_dir2, 0, 0]
action_final = []
copy = state.copy()
seq = []
state_space_final = new_states()
final_time = len(state_space_final)

while t< final_time:
    index = mapping[tuple(state)]
    action = p[t, index]
    seq.append(action)
    copy = state.copy()
    state = motion_model1(copy, str(dict_action[action]))
    t = t + 1
    action_final.append(dict_action[action])
    if state[0] == goal[0] and state[1] == goal[1]:
        break
seq.append(0)
print("Final Actions",action_final)
print("Final seq ",seq)
draw_gif_from_seq(seq, env, path="./gif/"+name_file+".gif")

