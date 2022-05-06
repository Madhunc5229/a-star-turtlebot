# a-star-turtlebot
This program is an implmentation of A-star algorithm for a turtlebot (burger).

## Dependencies
-   Python
-   Gazebo
-   ROS
-   Opencv 4.1.0
-   Numpy
-   queue

## Steps to run the package
1.Navigate to the source folder of your catkin workspace and clone the package
  
    cd catkin_ws/src
    git clone https://github.com/Madhunc5229/a-star-turtlebot
2.Build the package 

    cd ..
    cd catkin build

3.Launch the program which was simulated on real turtlebot
    
    roslaunch astar astar_comp.launch
    rosrun astar mainNode_comp

4.To launch the version which was used for simulation only:
  
    roslaunch astar astar.launch
    rorun astar mainNode
    
3.Program inputs
-  RPM values for the turtle bot (ex: 1,5)
-  start position - x,y,angle (fixed : 3,3,0) as the bot is spwaned using launch file
-  end postion  - x,y (ex: 90,90)
 
