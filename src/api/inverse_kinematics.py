from src.utils import Mentor
import numpy as np

if __name__ == "__main__":
    robot = Mentor()
    pos = np.zeros(3)
    angles = np.zeros(3)
    pos[0] = input('X 1')
    pos[1] = input('Y 1')
    pos[2] = input('Z 1')
    angles[0] = input('alpha')
    angles[1] = input('beta')
    angles[2] = input('gamma')
    angles[0] = 3.141592*angles[0]/180
    angles[1] = 3.141592*angles[1]/180
    angles[2] = 3.141592*angles[2]/180
    
    print('Thetas: ')
    print(robot.get_angles(pos,angles))
        