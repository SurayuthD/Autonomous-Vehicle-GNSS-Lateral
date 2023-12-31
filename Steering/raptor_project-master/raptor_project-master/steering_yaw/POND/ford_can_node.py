#!/usr/bin/env python3
import math
import time
import rospy
from transformations import quaternion_from_euler
from fordcan import FordCAN

from std_msgs.msg import *
from sensor_msgs.msg import *
from nav_msgs.msg import *

def on_gps(value):
    lat, lon = value
    m = NavSatFix()
    m.latitude = lat
    m.longitude = lon
    pub_gps.publish(m)

last_heading = 0.0
last_heading_time = 0
def on_heading(value):
    global last_heading, last_heading_time
    m = Float32()
    m.data = value
    last_heading = m.data
    last_heading_time = time.time()
    pub_heading.publish(m)

def on_accelerator_fraction(value):
    m = Float32()
    m.data = value
    pub_accelerator_fraction.publish(m)

def on_brake_pressure(value):
    m = Float32()
    m.data = value
    pub_brake_pressure.publish(m)

def on_ignition_switch(value):
    m = Int8()
    m.data = value
    pub_ignition_switch.publish(m)

def on_rpm(value):
    m = Float32()
    m.data = value
    pub_rpm.publish(m)

last_speed = 0.0
last_speed_time = 0
def on_speed(value):
    global last_speed, last_speed_time
    m = Float32()
    last_speed = m.data
    last_speed_time = time.time()
    m.data = value
    pub_speed.publish(m)

def on_steering_wheel_angle(value):
    m = Float32()
    m.data = value
    pub_steering_wheel_angle.publish(m)

def on_total_distance(value):
    m = Float32()
    m.data = value
    pub_total_distance.publish(m)

if __name__ == "__main__":
    rospy.init_node('ford_can_node')

    param_channel = rospy.get_param("~channel", "can0")
    param_bustype = rospy.get_param("~bustype", "socketcan_native")

    f = FordCAN(channel = param_channel, bustype = param_bustype)
    f.start()

    # raw data from canbus
    pub_accelerator_fraction = rospy.Publisher("accelerator_fraction", Float32, queue_size = 1)
    pub_brake_pressure = rospy.Publisher("brake_pressure", Float32, queue_size = 1)
    pub_gps = rospy.Publisher("gps/fix", NavSatFix, queue_size = 1)
    pub_heading = rospy.Publisher("gps/heading", Float32, queue_size = 1)
    pub_ignition_switch = rospy.Publisher("ignition_switch", Int8, queue_size = 1)
    pub_rpm = rospy.Publisher("rpm", Float32, queue_size = 1)
    pub_speed = rospy.Publisher("speed", Float32, queue_size = 1)
    pub_steering_wheel_angle = rospy.Publisher("steering_wheel_angle", Float32, queue_size = 1)
    pub_total_distance = rospy.Publisher("total_distance", Float32, queue_size = 1)

    # computed
    pub_odom = rospy.Publisher("odom", Odometry, queue_size = 1)

    f.on_accelerator_fraction = on_accelerator_fraction
    f.on_brake_pressure = on_brake_pressure
    f.on_gps = on_gps
    f.on_heading = on_heading
    f.on_ignition_switch = on_ignition_switch
    f.on_rpm = on_rpm
    f.on_speed = on_speed
    f.on_steering_wheel_angle = on_steering_wheel_angle
    f.on_total_distance = on_total_distance

    rospy.init_node('ford_can_node')
    current_x = 0.0
    current_y = 0.0
    current_yaw = 0.0

    msg_odom = Odometry()
    msg_odom.header.frame_id = "base_link"
    msg_odom.pose.covariance[6*0+0] = 1.0
    msg_odom.pose.covariance[6*1+1] = 1.0
    msg_odom.pose.covariance[6*2+2] = 1.0
    msg_odom.pose.covariance[6*3+3] = math.pi**2;
    msg_odom.pose.covariance[6*4+4] = math.pi**2;
    msg_odom.pose.covariance[6*5+5] = math.pi**2;
    msg_odom.twist.covariance[6*0+0] = 0.1;
    msg_odom.twist.covariance[6*1+1] = 0.0;
    msg_odom.twist.covariance[6*2+2] = 0.0;
    msg_odom.twist.covariance[6*3+3] = 0.0;
    msg_odom.twist.covariance[6*4+4] = 0.0;
    msg_odom.twist.covariance[6*5+5] = 0.04;

    rate = rospy.Rate(50)
    while not rospy.is_shutdown() and f.is_running:
        rate.sleep()

        t = time.time()
        if t - last_heading_time > 0.5 or t - last_speed_time > 0.5:
            rospy.logwarn("no heading/speed information in 0.5 s")
            continue
            
            current_yaw = -last_heading * math.pi / 180.0 # deg to rad
            current_lin_vel = last_speed / 3.6 # km/h to m/s
            current_ang_vel = 0.8 * current_ang_vel + 0.2 * (current_yaw - last_yaw) / 50.0
            last_yaw = current_yaw
            current_x += current_lin_vel / 50.0 * math.cos(current_yaw)
            current_y += current_lin_vel / 50.0 * math.sin(current_yaw)

            msg_odom.pose.pose.position.x = current_x
            msg_odom.pose.pose.position.y = current_y
            q = quaternion_from_euler(0.0, 0.0, current_yaw)
            msg_odom.pose.pose.orientation.w = q[0]
            msg_odom.pose.pose.orientation.x = q[1]
            msg_odom.pose.pose.orientation.y = q[2]
            msg_odom.pose.pose.orientation.z = q[3]
            msg_odom.twist.twist.linear.x = current_lin_vel
            msg_odom.twist.twist.angular.z = current_ang_vel
            pub_odom.publish(msg_odom)

    f.stop()