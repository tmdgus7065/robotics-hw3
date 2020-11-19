#!/usr/bin/env python
import rospy
from common_msgs.msg import Vectors

def callback(msg):
    print "subscribe:", msg.timetable.secs%100, msg.vect.x, msg.vect.y, msg.vect.z

rospy.init_node('Vectors_subscriber')
sub = rospy.Subscriber('common_msgs', Vectors, callback)
rospy.spin()
