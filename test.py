# pip3 install gym
# pip3 install gym[atari]
# sudo apt install python3-opengl

import gym
from multiprocessing import Process

def runGame(gameNum):
    env = gym.make('MsPacman-v0')
    print(env)
    env.reset()
    for k in range(10000):
        print(env.render(mode='rgb_array'))
        action = env.action_space.sample()
        while action not in [0, 2, 3, 4, 5]:
            action = env.action_space.sample()
        result = env.step(action) # take a random action
        print("Iteration " + str(k) + ", Action: " + str(action))
        #print(result)
        #print(result.observation)
        #print(result.reward)
        #print(result.done)
        #print(result.info)
        print(result[0])
        
        if result[1] > 0:
            print(result[1])

        if result[2] == True:
            break

    env.close()
    print("Game " + str(gameNum) + " complete")

if __name__ == '__main__':
    for i in range(1):
        p = Process(target=runGame, args=(i,))
        p.start()

