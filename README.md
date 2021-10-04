# Genetic Algorithms for Trajectory Optimization of the Mentor Robotic Arm


Here we submitted all code snippets to help with artificial intelligence coding to deal with an 
optimization problem, where the trajectory planning of a didactic robot is tackled.

See: `Makefile` to know other commands.

## Artificial Intelligence Project

==============================

Pipeline to generate trajectories for Mentor didactic robot using artificial intelligence optimization algorithms


Mentor is a Python library to implement a computational model of the Mentor Didactic Robotic Arm. This model was first published in the work *A Genetic Approach for Trajectory Optimization Applied to a Didactic Robot*. The library includes:

* Direct kinematics based on Denavit-Hartenberg parameters, where variables represented in the cartesian coordinate space are transformed to joint space.
* Inverse kinematics to encounter joint angles based on position and orientation matrix.
* Exception and error treatment in case of impossible position/orientation pairs.
* Method to deal with alpha, beta and gamma angles to encounter orientation 3x3 matrix based on XYZ angles.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install pymentor.

```bash
$ make
$ make install
```

## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.



```python
import numpy as np
from pymentor import Mentor
# direct kinematics example
angles = [np.pi/6]*5
robot = Mentor()
pos, rot = robot.get_position(angles)
# pos is 4x1 vector 
# rot is 3x3 rotation matrix
       
pos = np.array([24.21323027, 13.97951501, -17.07885504, 1.0])
rot = np.array([[0.59049287, 0.23642905, -0.77163428],
    [-0.23642905, -0.86349762, -0.44550326],
    [-0.77163428, 0.44550326, -0.4539905 ]])
# pos is 4x1 vector 
# rot is 3x3 rotation matrix
angles = robot.get_angles(pos,rot)


# creating rotational matrix from alpha-beta-gamma angles
rot = robot.get_orientation(np.pi/6, np.pi/6, np.pi/6)
```

## Contributing

Any contributions you make are **greatly appreciated**. To contribute please follow this steps:

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/new_feature`)
3. Commit your Changes (`git commit -m 'commit-tag: commit-description'`)
4. Push to the Branch (`git push origin feature/new_feature`)
5. Open a Pull Request

## License
General Public License version 3.0 [GPL-3.0](https://choosealicense.com/licenses/gpl-3.0/)

## Contact

Oscar Schmitt Kremer - [Linkedin](https://www.linkedin.com/in/oscar-kremer/) [Email](oscar.s.kremer@hotmail.com)

Project Link: [mentor-optimization Repository](https://github.com/oscarkremer/mentor-optimization)

## References

O. S. Kremer, M. A. B. Cunha, F. S. Moraes, S. S. Schiavon. *A Genetic Apporach for Trajectory Optimization Applied to a Didactic Robot* **2019 Latin American Robotics Symposium**. 2019.
[doi:10.1109/LARS-SBR-WRE48964.2019.00049](doi:10.1109/LARS-SBR-WRE48964.2019.00049)