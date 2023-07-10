# Optimal control using Dynamic Programming

<h1><b> Overview </b></h1>
This project focuses on path planning and the development of optimal control policies for robots or agents. Path planning involves finding a route from a starting location to a goal location while avoiding obstacles. Optimal control policies aim to minimize a cost function, such as energy consumption or task completion time, and are crucial for resource-efficient autonomous robots. The project implements a Dynamic Programming algorithm for autonomous navigation in a Door, Key, and Goal environment. <br>
The objective is to guide an agent to the goal while considering the possibility of encountering a closed door that requires a key to unlock. The project addresses both known and random map scenarios, calculating control policies for different environments. The results showcase the effectiveness of the proposed approach in calculating optimal control policies and demonstrate its potential application in autonomous navigation in complex environments.


<p align="center">
    <img src="https://github.com/dhruvtalwar18/optimal_control_dynamic_programming/blob/main/Results/gif/doorkey.gif" title="Sample control sequence" style="width: 600px; height: 600px;">
  <br>
  <p align="center">Fig.1 Sample Control sequence</p>
</p>



<h1><b> Known environment results </b></h1>

<table align="center">
  <tr>
    <td align="center">
      <img src="https://github.com/dhruvtalwar18/optimal_control_dynamic_programming/blob/main/Results/Known_envs/doorkey-5x5-normal.gif" title="Image 1" style="width: 300px; height: 300px;" loop>
      <br>
      <p align="center">Fig.1 5x5 normal</p>
    </td>
    <td align="center">
      <img src="https://github.com/dhruvtalwar18/optimal_control_dynamic_programming/blob/main/Results/Known_envs/doorkey-6x6-normal.gif" title="Image 2" style="width: 300px; height: 300px;">
      <br>
      <p align="center">Fig.2 6x6 Normal</p>
    </td>
    <td align="center">
      <img src="https://github.com/dhruvtalwar18/optimal_control_dynamic_programming/blob/main/Results/Known_envs/doorkey-6x6-direct.gif" title="Image 3" style="width: 300px; height: 300px;" autoplay loop muted>
      <br>
      <p align="center">Fig.3 6x6 Direct</p>
    </td>
  </tr>
  <tr>
    <td align="center">
      <img src="https://github.com/dhruvtalwar18/optimal_control_dynamic_programming/blob/main/Results/Known_envs/doorkey-8x8-direct.gif" title="Image 4" style="width: 300px; height: 300px;">
      <br>
      <p align="center">Fig.4 8x8 Direct</p>
    </td>
    <td align="center">
      <img src="https://github.com/dhruvtalwar18/optimal_control_dynamic_programming/blob/main/Results/Known_envs/doorkey-8x8-normal.gif" title="Image 5" style="width: 300px; height: 300px;">
      <br>
      <p align="center">Fig.5 8x8 Normal</p>
    </td>
    <td align="center">
      <img src="https://github.com/dhruvtalwar18/optimal_control_dynamic_programming/blob/main/Results/Known_envs/doorkey-8x8-shortcut.gif" title="Image 6" style="width: 300px; height: 300px;">
      <br>
      <p align="center">Fig.6 8x8 Shotcut</p>
    </td>
  </tr>
</table>

<br>


<h1><b> Samples from Unknown environment results </b></h1>

<table align="center">
  <tr>
    <td align="center">
      <img src="https://github.com/dhruvtalwar18/optimal_control_dynamic_programming/blob/main/Results/Unknown_envs/DoorKey-8x8-12.gif" title="Image 1" style="width: 300px; height: 300px;" loop>
      <br>
      <p align="center">Fig.1 Sample 1</p>
    </td>
    <td align="center">
      <img src="https://github.com/dhruvtalwar18/optimal_control_dynamic_programming/blob/main/Results/Unknown_envs/DoorKey-8x8-16.gif" title="Image 2" style="width: 300px; height: 300px;">
      <br>
      <p align="center">Fig.2 Sample 2</p>
    </td>
    <td align="center">
      <img src="https://github.com/dhruvtalwar18/optimal_control_dynamic_programming/blob/main/Results/Unknown_envs/DoorKey-8x8-2.gif" title="Image 3" style="width: 300px; height: 300px;" autoplay loop muted>
      <br>
      <p align="center">Fig.3 Sample 3</p>
    </td>
  </tr>
  <tr>
    <td align="center">
      <img src="https://github.com/dhruvtalwar18/optimal_control_dynamic_programming/blob/main/Results/Unknown_envs/DoorKey-8x8-24.gif" title="Image 4" style="width: 300px; height: 300px;">
      <br>
      <p align="center">Fig.4 Sample 4</p>
    </td>
    <td align="center">
      <img src="https://github.com/dhruvtalwar18/optimal_control_dynamic_programming/blob/main/Results/Unknown_envs/DoorKey-8x8-30.gif" title="Image 5" style="width: 300px; height: 300px;">
      <br>
      <p align="center">Fig.5 Sample 5</p>
    </td>
    <td align="center">
      <img src="https://github.com/dhruvtalwar18/optimal_control_dynamic_programming/blob/main/Results/Unknown_envs/DoorKey-8x8-36.gif" title="Image 6" style="width: 300px; height: 300px;">
      <br>
      <p align="center">Fig.6 Sample 6</p>
    </td>
  </tr>
</table>



<h1><b> Code Setup </b></h1>

Create a conda environment 
```
conda create -name optimal_control
conda activate optimal_control
git clone https://github.com/dhruvtalwar18/optimal_control_dynamic_programming
cd optimal_control_dynamic_programming
pip install -r requirements.txt

```


<h2> Helper functions </h2>

1. utils.py
The file utils.py contains several helpful tools that you may find useful for your project.

The step() function allows you to move your agent within the environment.
The generate_random_env() function generates a random environment that can be used for debugging purposes.
The load_env() function is used to load pre-defined test environments.
The save_env() function enables you to save the current environment for later reproduction of results.
The plot_env() function provides a convenient way to visualize your current environment, including the agent, key, door, and goal.
Lastly, the draw_gif_from_seq() function allows you to generate and save a gif image based on a given action sequence.


2. example.py
You can refer to the example.py file to learn how to use the utilities provided in utils.py and interact with the gym-minigrid library. The example.py file serves as a guide and provides examples of how to effectively utilize the utilities and work with the gym-minigrid environment

<h2> Main Functions </h2>
Part A
In the known_envs folder run the main.py file, it takes its path from path_names_.py file and the motion model and stage cost is defined in motion_model_.py and stage_cost_.py respectively. 
This script is used to implement Dynamic Programming on the environments specified in Part A. There are seven different parts in A, and this code will create the shortest paths for each of the environments. Usage:

```
python3 main.py

```
Part B
In the unknown_envs folder run the final_part_b.py file this script is used to implement Dynamic Programming on the environments specified in Part B. This program creates a single policy function for all the maps in Part B and creates the shortest path for any environment in this from the single policy function. Usage :

```
python3 final_part_b.py

```
