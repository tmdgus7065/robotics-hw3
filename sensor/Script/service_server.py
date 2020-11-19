#!/usr/bin/env python
import rospy
from common_msgs.srv import AddFourNum, AddFourNumResponse

def service_callback(request):
    response = AddFourNumResponse(sum=request.a + request.b + request.c + request.d)
    print "EachWheel data:", request.a, request.b, request.c, request.d, ", SumOf4Wheel:", response.sum
    return response

rospy.init_node('service_server')
service = rospy.Service('add_four_number', AddFourNum, service_callback)
rospy.spin()
