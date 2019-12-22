#!/usr/bin/python3
import rospy
from turtlesim.srv import SetPen
from turtlesim.srv import TeleportAbsolute
from turtlesim.srv import TeleportRelative
from math import pi

nums = [
[[1, 0], [-1, 0], [1, pi/2], [1, -pi/2], [1, pi/2], [1, pi/2]],
[[1, 0], [1, pi/2], [1, pi/2], [1, -pi/2], [1, -pi/2]],
[[1, 0, 0], [2, pi/2]]
]

def answer(inp):
global setpen, rel, abso
rospy.init_node('labturtle', anonymous=True)
rospy.wait_for_service('turtle1/set_pen')
setpen = rospy.ServiceProxy('turtle1/set_pen', SetPen)
rospy.wait_for_service('turtle1/teleport_absolute')
abso = rospy.ServiceProxy('turtle1/teleport_absolute', TeleportAbsolute)
rospy.wait_for_service('turtle1/teleport_relative')
rel = rospy.ServiceProxy('turtle1/teleport_relative', TeleportRelative)
c = 0
for i in inp.split():
single(i, c)
c+=1

def single(num, offset):
global setpen, t_tpr, t_tpa
setpen(102, 51, 0, 7, 1)
x = 0.25 + offset * 11.0 / 6.0; y = 4.0
abso(x, y, 0)
setpen(102, 51, 0, 7, 0)
for coords in nums[int(num)]:
if len(coords)==2:
setpen(200, 7, 1, 2, 0)
rel(coords[0], coords[1])
else:
setpen(200, 7, 1, 2, 1)
rel(coords[0], coords[1])

if __name__ == '__main__':
try:
answer("0 0 1 0 2 2")
except rospy.ROSInterruptException:
pass
