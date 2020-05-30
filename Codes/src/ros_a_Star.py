# -*- coding: utf-8 -*-
# Credits: https://github.com/markwsilliman/turtlebot

import rospy
from geometry_msgs.msg import Twist
import numpy as np
import time


class a_Star():
    def __init__(self, path):
        rospy.init_node('pathFollow', anonymous=False)
        rospy.loginfo("To stop TurtleBot CTRL + C")
        rospy.on_shutdown(self.shutdown)
        self.cmd_vel = rospy.Publisher('cmd_vel_mux/input/navi', Twist, queue_size=10)
        rad = 0.038
        l = 0.230
        dt = 5
        zero_cmd = Twist()
        r = rospy.Rate(10);
        move_cmd = Twist()
        count = 1
        while not rospy.is_shutdown() and count < path.shape[0]:
            ur = path[count][1]
            ul = path[count][2]
            theta = path[count][0]
            print(ul,ur,theta)
            loop_time = 0
            print((ur+ul)*rad/2)
            print((ur-ul)*rad/l)
            for i in range(0,10):
                move_cmd.linear.x = (ur+ul)*rad/2 * 0.9
                move_cmd.angular.z = (ur-ul)*rad/l * 1.4
                self.cmd_vel.publish(move_cmd)
                r.sleep()
            self.cmd_vel.publish(zero_cmd)
            r.sleep()
            print(count)
            count = count +1

    def shutdown(self):
        rospy.loginfo("Stop TurtleBot")
        self.cmd_vel.publish(Twist())
        rospy.sleep(1)

if __name__ == '__main__':
    file = open("path.txt", "r").read()
    path = np.array(file.split())
    col = 3
    row = path.shape[0]/col
    print(row)
    path = np.reshape(path, (row, col))
    path = path.astype(np.float64)
    print(path)

    try:
        a_Star(path)
    except:
        rospy.loginfo("GoForward node terminated.")
