from core_tool import *

def Help():
        return '''Move arm to target joint angles.
        Then move fingers of gripper to a target position.
        Usage: 
        '''
def Run(t,*args):
        filef = open("/home/hm/ros_ws/lfd_trick/scripts/motions/hm17/painting/coords.txt", "r")
        arr = filef.readlines()

        curr = list(t.robot.FK(arm=LEFT))
        t_traj =[0.0]
        x_traj =[curr]
        for index in range(len(arr)):
                moveto_arr = []
                temp = arr[index].split(" ")
                x_trg = curr[0]+float(temp[0])*0.33
                y_trg = curr[1]+float(temp[1])*0.33
                x_dir = 1
                y_dir = 1
                tempcurr = x_traj[-1]
                if(x_trg < tempcurr[0]):
                        x_dir = -1
                if(y_trg < tempcurr[1]):
                        y_dir = -1

                numsteps = 3
                x_diff = x_dir*(x_trg-tempcurr[0])/numsteps
                y_diff = y_dir*(y_trg-tempcurr[1])/numsteps

                for i in range(numsteps):
                        blahx = tempcurr[0]+(x_diff*(i+1)*x_dir)
                        blahy = tempcurr[1]+(y_diff*(i+1)*y_dir)
                        x_traj.append([blahx, blahy]+tempcurr[2:])
                        t_traj.append(t_traj[-1]+0.8)
                        print([blahx, blahy])

        print("x", x_traj)
        print("t", t_traj)
        t.robot.FollowXTraj(x_traj, t_traj, arm=LEFT)
        print("finito")
