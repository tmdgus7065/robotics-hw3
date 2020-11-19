#!/usr/bin/env python
import rospy
from common_msg.msg import Vectors
from geometry_msgs.msg import Vector3

rospy.init_node('Vectors_publisher')
pub = rospy.Publisher('common_msgs', Vectors, queue_size=1)
msg = Vectors()
rate = rospy.Rate(1)
while not rospy.is_shutdown():
    msg.timetable = rospy.get_rostime()
    second = msg.timetable.secs
    msg.inc = vect(x=second%2, y=second%3, z=second%4)
    pub.publish(msg)
    print "publish", msg.timetable.secs%100, msg.inc.x, msg.inc.y, msg.inc.z
    rate.sleep()

