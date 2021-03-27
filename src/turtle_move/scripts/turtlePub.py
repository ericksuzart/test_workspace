#!/usr/bin/env python

import rospy

from geometry_msgs.msg import Twist

def pub_Function():
    # Twist = classe de mensagem
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size = 10)
    rospy.init_node('TurtelMoveNode', anonymous=False)

    taxa = rospy.Rate(2)

    topic_msg = Twist()
    
    topic_msg.linear.x = 1
    topic_msg.linear.y = 0
    topic_msg.angular.z = 0.3

    while not rospy.is_shutdown():
        pub.publish(topic_msg)
        taxa.sleep()
    

if __name__ == '__main__':
    try:
        pub_Function()
    except rospy.ROSInterruptException:
        pass