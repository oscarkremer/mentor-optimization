import argparse
import gym

def build_arg_parser():
    parser = argparse.ArgumentParser(description='Run an environment')
    parser.add_argument('--input-env', dest='input_env', required=True,
                        choices=['cartpole', 'mountaincar', 'pendulum'],
                        help='Specify the name of the environment')

    return parser

if __name__=='__main__':

    args = build_arg_parser().parse_args()
    input_env = args.input_env
    name_map = {'cartpole': 'CartPole-v0',
                'mountaincar': 'MountainCar-v0',
                'pendulum': 'Pendulum-v0'}

    # Create the environment and reset it
    env = gym.make(name_map[input_env])

    # Start iterating
    for _ in range(200000):
        # Reset the environment
        observation = env.reset()
        # Print the current observation
        for i in range(100000000):
            #Render the environment
            env.render()
            print(observation)
            # Take action
            action = env.action_space.sample()
            # Extract the observation, reward, status and
            # other info based on the action taken
            observation, reward, done, info = env.step(action)

            #if done:
            #    print('Episode finished after {} timesteps'.format(i+1))
            #    break
