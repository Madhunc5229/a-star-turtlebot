#!/usr/bin/env python

import rospy
import argparse
from std_msgs.msg import String
import geometry_msgs.msg
from queue import PriorityQueue

def polygonOpen():

  #-----------------------------------------------------------------------------
  # Initialize node
  #-----------------------------------------------------------------------------

  rospy.init_node('open_polygon', anonymous=False)

  # This code is required to make sure this node gets simulation time correctly
  simulation = False
  if rospy.has_param('/use_sim_time'):
    if rospy.get_param("/use_sim_time") == True:
      simulation = True

  if simulation:
    rospy.loginfo("Using simulated time.")
    rospy.loginfo("Waiting for the first valid time measurement...")
    t = rospy.Time.now()
    while t == rospy.Time.from_sec(0):
      t = rospy.Time.now()
    rospy.loginfo("Done!")

  else:
    rospy.loginfo("Using real time.")

  #-----------------------------------------------------------------------------
  # Parse command line
  #-----------------------------------------------------------------------------

  parser = argparse.ArgumentParser(description='Polygon Drive Openloop Control')
  parser.add_argument('-d',      default=0.2, type=float)
  parser.add_argument('-n',      default=6, type=int)

  args = parser.parse_args()
  sideLength = args.d
  numSides = args.n

  rospy.loginfo("Polygon parameters:")
  rospy.loginfo("  number of sides: " + str (numSides))
  rospy.loginfo("  side length: " + str(sideLength))

  #-----------------------------------------------------------------------------
  # Drive (your code should go here)
  #-----------------------------------------------------------------------------

  #Messgaes will be published on topic... & message type will be...
  pub = rospy.Publisher('/cmd_vel',geometry_msgs.msg.Twist, queue_size=10)

  #Parameters: linear velocity (v) in m/s and angular velocity (w) in rad/s
  v = 0.5
  w = 0.5

  #Message and time for straight movement along the side of polygon
  msg1 = geometry_msgs.msg.Twist()
  msg1.linear.x = v

  duration1 = sideLength/msg1.linear.x

  #Message and time for rotation at the corner of polygon
  msg2 = geometry_msgs.msg.Twist()
  msg2.angular.z = w

  angleOfRotation = 6.28/numSides
  duration2 = angleOfRotation/msg2.angular.z

  #Sending a message (msg) for amount of time (number_of_seconds)
  def send_msg_block(number_of_seconds,msg):

    r = rospy.Rate(10)
    t = rospy.Time.now()

    while rospy.Time.now() - t < rospy.Duration(number_of_seconds):
      pub.publish(msg)
      r.sleep()

  #For each side, go straight & turn
  for i in range(numSides):

    send_msg_block(duration1,msg1)
    send_msg_block(duration2,msg2)




#-------------------------------------------------------------------------------
# Main
#-------------------------------------------------------------------------------

if __name__ == '__main__':
  try:
    polygonOpen()
  except rospy.ROSInterruptException:
    pass
