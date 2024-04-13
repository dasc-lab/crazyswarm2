import numpy as np
import pandas
from crazyflie_py import Crazyswarm
import matplotlib.pyplot as plt

if __name__ == '__main__':
    data = pandas.read_csv('./data/crazyflies_data_3_new_mobile.csv', quotechar='"').values

    pos1 = data[:, 0:7]
    pos2 = data[:, 14:21]
    pos3 = data[:, 28:35]
    pos4 = data[:, 42:49]

    takeoffHeight = 0.5
    startingHeight = 0.12
    offsetStart = 0.20



    pos1[0,2] = pos1[0,2] + offsetStart
    pos2[0,2] = pos2[0,2] + offsetStart
    pos3[0,2] = pos3[0,2] + offsetStart

    pos1[1:,2] = pos1[1:,2] + startingHeight
    pos2[1:,2] = pos2[1:,2] + startingHeight
    pos3[1:,2] = pos3[1:,2] + startingHeight
    # pos4[:,2] = pos4[:,2] + startingHeight

    n = 40
    pos1 = pos1[::n]
    pos2 = pos2[::n]
    pos3 = pos3[::n]
    # pos4 = pos4[::n]

    print(pos1[:,2])
    idx_lowest = np.argmin(pos1[1:,2]) + 1
    print(idx_lowest)
    input()

    swarm = Crazyswarm()
    print(swarm.allcfs.crazyflies[0].prefix)
    print(swarm.allcfs.crazyflies[1].prefix)
    # print(swarm.allcfs.crazyflies[2].prefix)
    timeHelper = swarm.timeHelper
    allcfs = swarm.allcfs

    allcfs.takeoff(targetHeight=takeoffHeight, duration = 6.0)
    timeHelper.sleep(1.0+5.0)

    duration_increase = 0.0
    for i in range(pos1.shape[0]):
        if i < 5:
            duration = 4.0
        else:
            duration = 2.2

        if i >= idx_lowest:
            duration_increase = 0.1
        allcfs.crazyflies[0].goTo(pos1[i],0,duration+duration_increase)
        allcfs.crazyflies[1].goTo(pos2[i],0,duration+0.2)
        # allcfs.crazyflies[2].goTo(pos2[i],0,duration)
        # allcfs.crazyflies[1].goTo(pos3[i],0,duration)
        timeHelper.sleep(duration)
    
    allcfs.land(targetHeight=0.02, duration=6.0)
    timeHelper.sleep(6.0)