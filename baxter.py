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
        #t.robot.MoveToX([tempcurr[0], tempcurr[1], tempcurr[2]-0.2]+tempcurr[3:], dt=3.0, arm=LEFT)

        for index in range(0):
                #curr = list(t.robot.FK(arm=LEFT))
                moveto_arr = []
                temp = arr[index].split(" ")
                x = curr[0]-float(temp[0])
                y = curr[1]-float(temp[1])
                moveto_arr.append(x)
                moveto_arr.append(y)
                moveto_arr.append(curr[2])
                moveto_arr += curr[3:]

                print("1",moveto_arr)
                t.robot.MoveToX(moveto_arr, dt=3.0, arm=LEFT)

                x = curr[0]-float(temp[2])
                y = curr[1]-float(temp[3])
                moveto_arr2 = [x,y,curr[2]] + curr[3:]
                print("2",moveto_arr2)
                t.robot.MoveToX(moveto_arr2, dt=3.0, arm=LEFT)

        t.robot.MoveToX(curr, dt=3.0, arm=LEFT)
        print("finito")

