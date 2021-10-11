# Genetic Algorithms for Trajectory Optimization of the Mentor Robotic Arm


Here we submitted all code snippets to help with artificial intelligence coding to deal with an 
optimization problem, where the trajectory planning of a didactic robot is tackled.

See: `Makefile` to know other commands.

## Artificial Intelligence Project

==============================

Pipeline to generate trajectories for Mentor didactic robot using artificial intelligence optimization, more specifically genetic algorithms. This model was 
first published in the work *A Genetic Approach for Trajectory Optimization Applied to a Didactic Robot*, together with the results for modeling direct and inverse
kinematics of the mentor robotics arms, which resulted in the [pymentor package](https://github.com/oscarkremer/pymentor). 

## Installation

To run the scripts presented in this repository one can install it using the following command:

```bash
$ make install
```

It's essential to have installed the miniconda or anaconda, where a virtual environment entitled as *mentor-optimization* will be created. 

## Usage

After running the *make install* command, one can try the genetic optimization proposed. However, first is necessary to run the following command in the terminal:

```bash
$ conda activate mentor-optimization
```

Inside the project folder the *help* command can be used to see all available make commands.

```bash
$ make help
```

To run genetic optimization use the following command:

```bash
$ make genetic
```

Insert the initial and final position.


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