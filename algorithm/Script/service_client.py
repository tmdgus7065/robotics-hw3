#!/usr/bin/env python
import rospy
from common_msgs.srv import AddFourNum, AddFourNumRequest

rospy.init_node('service_client')
rospy.wait_for_service('add_four_number')
requester = rospy.ServiceProxy('add_four_number', AddFourNum)
print "requester type:", type(requester), ", callable?", callable(requester)
rate = rospy.Rate(10)
count = 0
while count < 200:
    if count % 10 == 0:
        print count, "times turned!!!! Cheer Up!!!!!!!!"
    if count % 1 == 0:
        req = AddFourNumRequest(a=count, b=count, c=count, d=count)
        res = requester(req)
        print count, "EachWheel:", req.a, req.b, req.c, req.d, "SumOf4Wheel:", res.sum
    rate.sleep()
    count += 1
