#!/usr/bin/env python
import roslib
roslib.load_manifest('spatulasss')
import rospy
import tf

if __name__ == '__main__':
    rospy.init_node('my_spatula_broadcaster')
    br = tf.TransformBroadcaster()
    rate = rospy.Rate(10.0)
    while not rospy.is_shutdown():
       br.sendTransform((0.001, -0.002, 0.025), (0.0, 0.0, 0.0, 1.0), rospy.Time.now(), "spatula_link", "l_gripper_tool_frame")
       rate.sleep()
