from core_tool import *

def Help():
	return '''Move arm to target joint angles.
	Then move fingers of gripper to a target position.
	Usage: 
	  POSE: Array of target pose = [x,y,z,qx,qy,qz,qw] (position, quaternion)
	'''

def Run(t,*args):
	file = open("coords.txt", "r")
	arr = file.readlines()
	curr = list(t.robot.FK(arm=arm))
	for index in range(len(arr)):
		moveto_arr = []
		temp = index.split(" ")
		x = float(temp[0])
		y = float(temp[1])
		moveto_arr.append(x)
		moveto_arr.append(y)
		moveto_arr.append(curr[2])

		#inverse kinematics
		#x_trg = arr[index]
		#IK = t.robot.IK(x_trg, arm=arm) #target joint angles

		#move arm
		#q_traj = [
			#q, 
			#[q[d]+(0.1,0.0,0.0,0.0,0.0,0.0,0.0)[d] for d in range(7)],
			#[q[d]+(-0.1,0.0,0.0,0.0,0.0,0.0,0.0)[d] for d in range(7)],
			#[q[d]+(0.0,0.1,0.0,0.0,0.0,0.0,0.0)[d] for d in range(7)],
			#[q[d]+(0.0,-0.1,0.0,0.0,0.0,0.0,0.0)[d] for d in range(7)],
			#q
		#]
		#t.robot.FollowQTraj(q_traj, [0.0, 2.0, 4.0, 6.0, 8.0, 10.0], arm)
		t.robot.MoveToX(moveto_arr, dt=4.0, arm=LEFT)

	print "finito"
