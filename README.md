# Optimal control using Dynamic Programming

<h1><b> Overview </b></h1>
This project focuses on path planning and the development of optimal control policies for robots or agents. Path planning involves finding a route from a starting location to a goal location while avoiding obstacles. Optimal control policies aim to minimize a cost function, such as energy consumption or task completion time, and are crucial for resource-efficient autonomous robots. The project implements a Dynamic Programming algorithm for autonomous navigation in a Door, Key, and Goal environment. <br>
The objective is to guide an agent to the goal while considering the possibility of encountering a closed door that requires a key to unlock. The project addresses both known and random map scenarios, calculating control policies for different environments. The results showcase the effectiveness of the proposed approach in calculating optimal control policies and demonstrate its potential application in autonomous navigation in complex environments.


<p align="center">
    <img src="https://github.com/dhruvtalwar18/optimal_control_dynamic_programming/blob/main/Results/gif/doorkey.gif" title="Sample control sequence" style="width: 600px; height: 600px;">
  <br>
  <p align="center">Fig.1 Sample Control sequence</p>
</p>



<h1><b> Known and Unknown environment results </b></h1>

<table align="center">
  <tr>
    <td align="center">
      <img src="https://github.com/dhruvtalwar18/optimal_control_dynamic_programming/blob/main/Results/Known_envs/doorkey-5x5-normal.gif" title="Image 1" style="width: 300px; height: 300px;" loop>
      <br>
      <p align="center">Fig.1 Image 1</p>
    </td>
    <td align="center">
      <img src="https://github.com/dhruvtalwar18/optimal_control_dynamic_programming/blob/main/Results/Known_envs/doorkey-6x6-normal.gif" title="Image 2" style="width: 300px; height: 300px;">
      <br>
      <p align="center">Fig.2 Image 2</p>
    </td>
    <td align="center">
      <img src="https://github.com/dhruvtalwar18/optimal_control_dynamic_programming/blob/main/Results/Known_envs/doorkey-6x6-direct.gif" title="Image 3" style="width: 300px; height: 300px;" autoplay loop muted>
      <br>
      <p align="center">Fig.3 Image 3</p>
    </td>
  </tr>
  <tr>
    <td align="center">
      <img src="https://github.com/dhruvtalwar18/optimal_control_dynamic_programming/blob/main/Results/Known_envs/doorkey-8x8-direct.gif" title="Image 4" style="width: 300px; height: 300px;">
      <br>
      <p align="center">Fig.4 Image 4</p>
    </td>
    <td align="center">
      <img src="https://github.com/dhruvtalwar18/optimal_control_dynamic_programming/blob/main/Results/Known_envs/doorkey-8x8-normal.gif" title="Image 5" style="width: 300px; height: 300px;">
      <br>
      <p align="center">Fig.5 Image 5</p>
    </td>
    <td align="center">
      <img src="https://github.com/dhruvtalwar18/optimal_control_dynamic_programming/blob/main/Results/Known_envs/doorkey-8x8-shortcut.gif" title="Image 6" style="width: 300px; height: 300px;">
      <br>
      <p align="center">Fig.6 Image 6</p>
    </td>
  </tr>
</table>







<h1><b> Code Setup </b></h1>


