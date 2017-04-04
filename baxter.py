from core_tool import *

def Help():
	return '''Move arm to target joint angles.
	Then move fingers of gripper to a target position.
	Usage: 
	  POSE: Array of target pose = [x,y,z,qx,qy,qz,qw] (position, quaternion)
	'''

def Run(t,*args):
	#inverse kinematics
	arm = LEFT
	x_trg = args[1]
	IK = t.robot.IK(x_trg, arm=arm) #target joint angles

	#move arm
	q = list(t.robot.Q(arm=arm))  #Current joint angles
	q_traj = [
		q, 
		[q[d]+(0.1,0.0,0.0,0.0,0.0,0.0,0.0)[d] for d in range(7)],
		[q[d]+(-0.1,0.0,0.0,0.0,0.0,0.0,0.0)[d] for d in range(7)],
		[q[d]+(0.0,0.1,0.0,0.0,0.0,0.0,0.0)[d] for d in range(7)],
		[q[d]+(0.0,-0.1,0.0,0.0,0.0,0.0,0.0)[d] for d in range(7)],
		q
	]
	t.robot.FollowQTraj(q_traj, [0.0, 3.0, 6.0, 9.0, 12.0, 15.0], arm)

	print "finito"