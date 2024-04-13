#!/usr/bin/env python

from crazyflie_py import Crazyswarm
import numpy as np


def main():
    Z = 1.0
    L = 1.0
    T = 4.0

    swarm = Crazyswarm()
    timeHelper = swarm.timeHelper
    allcfs = swarm.allcfs

    allcfs.takeoff(targetHeight=Z, duration=1.0+3.0)
    timeHelper.sleep(1.5+Z)
    for cf in allcfs.crazyflies:
        pos = np.array(cf.initialPosition) + np.array([0, 0, Z])
        cf.goTo(pos, 0, 1.0)
    timeHelper.sleep(T)
    
    for cf in allcfs.crazyflies:
        pos = np.array(cf.initialPosition) + np.array([L, 0, Z])
        cf.goTo(pos, 0, T)
    timeHelper.sleep(T)

    for cf in allcfs.crazyflies:
        pos = np.array(cf.initialPosition) + np.array([L, L, Z])
        cf.goTo(pos, 0, T)
    timeHelper.sleep(T)

    for cf in allcfs.crazyflies:
        pos = np.array(cf.initialPosition) + np.array([0, L, Z])
        cf.goTo(pos, 0, T)
    timeHelper.sleep(T)

    for cf in allcfs.crazyflies:
        pos = np.array(cf.initialPosition) + np.array([0, 0, Z])
        cf.goTo(pos, 0, T)
    timeHelper.sleep(T)

    allcfs.land(targetHeight=0.02, duration=1.0+3.0)
    timeHelper.sleep(1.0+Z)


if __name__ == '__main__':
    main()
