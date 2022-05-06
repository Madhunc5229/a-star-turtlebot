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
 
## Action space for non-holonomic robot considered for generating nodes
![image](https://user-images.githubusercontent.com/61328094/167195443-c6ad7bf6-a069-4629-a74b-629e35475e23.png)

### Video link for output of A-star implementation on burger turtlebot3 : https://youtube.com/shorts/tdTCO5UjJfM?feature=share

## Output
![image](https://user-images.githubusercontent.com/61328094/167198002-a4b0a08e-c18e-440f-8571-a1e852efd617.png)


