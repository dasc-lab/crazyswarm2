#!/usr/bin/env python

from pathlib import Path

from crazyflie_py import Crazyswarm
import numpy as np


def main():
    Z = 1.0
    T0 = 2.0
    T = 5.0
    filepath = Path(__file__).parent / 'data/traj_pts.csv'
    traj_pts = np.loadtxt(filepath, delimiter=',', skiprows=1).T

    swarm = Crazyswarm()
    timeHelper = swarm.timeHelper
    allcfs = swarm.allcfs   

    allcfs.takeoff(targetHeight=Z, duration=1.0+T0)
    timeHelper.sleep(1.5+T0)
    for cf in allcfs.crazyflies:
        pos = np.array(cf.initialPosition) + np.array([0,0,Z])
        cf.goTo(pos, 0, T0)
    timeHelper.sleep(T0)

    for i in range(traj_pts.shape[1]):
        trajectory = traj_pts[:,i]
        for cf in allcfs.crazyflies:
            pos = np.array(cf.initialPosition) + trajectory[:3] + np.array([0,0,Z])
            cf.goTo(pos, 0, T)
        timeHelper.sleep(T)
    
    allcfs.land(targetHeight=0.02, duration=1.0+Z)
if __name__ == '__main__':
    main()