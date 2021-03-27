#!/usr/bin/env python

import rospy

from geometry_msgs.msg import Twist

def twistCallback (mensagem):
    rospy.loginfo("Tem alguem movendo o TurtleBot!\n")
    rospy.loginfo(mensagem)

def subFunction():
    rospy.init_node("SubNode",anonymous=False)

    rospy.Subscriber('/turtle1/cmd_vel', Twist, twistCallback)

    rospy.spin() #fica esperando mensagem

if __name__ == '__main__':
    try:
        subFunction()
    except rospy.ROSInterruptException():
        pass
