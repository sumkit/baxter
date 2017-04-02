from core_tool import *

def Help():
	return '''Move arm to target joint angles.
	Then move fingers of gripper to a target position.
	Usage: 
	  ARM: RIGHT or LEFT. default=t.robot.Arm
	  POSE: Array of target pose = [x,y,z,qx,qy,qz,qw] (position, quaternion)
	'''

def Run(t,*args):
	#move arm
	arm = args[0]
	dq = args[1]
	q = t.robot.Q(arm=arm)  #Current joint angles
	q_trg = [q[d]+dq[d] for d in range(7)]  #Target
	t.robot.MoveToQ(q_trg, dt=4.0, arm=arm)

	#move fingers
	pos = args[1]
	t.robot.MoveGripper(pos, arm=arm)
	return 