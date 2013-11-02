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
       br.sendTransform((0.01, -0.03, 0.05), (0.0, 0.0, 0.0, 1.0), rospy.Time.now(), "spatula_link", "l_gripper_l_finger_tip_link")
       rate.sleep()
