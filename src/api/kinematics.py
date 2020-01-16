import numpy as np
from src.utils import Mentor
from src.utils.input import input_angles

if __name__ == "__main__":
    robot = Mentor()
    angles  = input_angles()
    pos, rot = robot.get_position(angles)
    print('Position Vector: ')
    print(pos)
    print('Rotation Matrix: ')
    print(rot)
    print('Thetas: {}'.format(180*np.array(robot.get_angles(pos,rot))/np.pi))
        