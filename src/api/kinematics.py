from src.utils import Mentor
import numpy as np

if __name__ == "__main__":
    robot = Mentor()
    angles = np.zeros(5)
    angles[0] = input('Theta 1')
    angles[1] = input('Theta 2')
    angles[2] = input('Theta 3')
    angles[3] = input('Theta 4')
    angles[4] = input('Theta 5')


    pos, rot = robot.get_position(angles, 0)
    print('Position: ')
    print(pos)
    print('Rotation Matrix: ')
    print(rot)
    print('Thetas: ')
    print(robot.get_angles(pos,rot))
        