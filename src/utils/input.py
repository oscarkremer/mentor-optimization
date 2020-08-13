import numpy as np

def input_angles():
    angles = np.zeros(5)
    for i in range(5):
        angles[i] = input('-- Theta {}: '.format(i+1))
        angles[i] = np.pi*angles[i]/180
    return angles

def input_cartesian():
    pos = np.zeros(3)
    angles = np.zeros(3)
    pos[0] = input('-- x (cm): ')
    pos[1] = input('-- y (cm): ')
    pos[2] = input('-- z (cm): ')
    angles[0] = input('-- alpha: ')
    angles[1] = input('-- beta: ')
    angles[2] = input('-- gamma: ')
    angles[0] = np.pi*angles[0]/180
    angles[1] = np.pi*angles[1]/180
    angles[2] = np.pi*angles[2]/180
    return pos, angles