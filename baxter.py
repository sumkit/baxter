from core_tool import *

def Help():
	return '''Move arm to target joint angles.
	Then move fingers of gripper to a target position.
	Usage: 
	  POSE: Array of target pose = [x,y,z,qx,qy,qz,qw] (position, quaternion)
	'''

def Run(t,*args):
	# file = open("coords.txt", "r")
	# arr = file.readlines()
	arr = ["0.2 0.2", "0.3 0.3", "0.4 0.4", "0.5 0.5", "0.6 0.6", "0.7 0.7"]
	curr = list(t.robot.FK(arm=arm))
	for index in range(len(arr)):
		moveto_arr = []
		temp = index.split(" ")
		x = float(temp[0])
		y = float(temp[1])
		moveto_arr.append(x)
		moveto_arr.append(y)
		moveto_arr.append(curr[2]) #keep z coordinate constant
		t.robot.MoveToX(moveto_arr, dt=4.0, arm=LEFT)

	print "finito"
