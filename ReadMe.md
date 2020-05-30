# A-star in non-holonomic robot

## Instructions to run the program.

Setting up the workspace:

1) Unzip ths project folder.
2) Copy the files inside Codes folder to your ros workspace
3) If the ros workspace is not set up, Look into this website to build your workspace. 
http://wiki.ros.org/ROS/Tutorials/InstallingandConfiguringROSEnvironment


A Star Implementaion:

1) Run the pathPlanning.py script, which is located inside the src folder
2) Enter the coordinates of start and goal points.
3) If it is entered wrongly, then program will prompt user to enter it again.
4) It will generate path.txt, which will be used in simulation.


Gazebo Simulation:
1) Open your ros workspace.
2) Type the following commands.
	```
	source devel/setup.bash
	roslaunch a_star_turtlebot a_star_turtlebot.launch
	```
3) Once gazebo is launched, drag the turtle to the start position mentioned in the A Star Implementation.
4) Then, navigate to src folder inside the workspace and run the ros_a_star.py script.


