# pip3 install gym
# pip3 install gym[atari]
# sudo apt install python3-opengl

import gym
import multiprocessing
import time

# Change these as you'd like
RENDER_GAME = False
NUM_GAMES = 10

def runGame(gameNum, results):
    env = gym.make('MsPacman-v0')
    score = 0
    env.reset()
    print("Starting game " + str(gameNum))

    for k in range(10000):

        action = env.action_space.sample()
        while action not in [0, 2, 3, 4, 5]:
            action = env.action_space.sample()
        result = env.step(action) # take a random action

        #print(result)
        #print(result.observation)
        #print(result.reward)
        #print(result.done)
        #print(result.info)
        #print(result[0])

        #print(env.render(mode='rgb_array'))
        if RENDER_GAME:
            env.render()
            print("Iteration " + str(k) + ", Action: " + str(action) + ", Current Score: " + str(score))

        score = score + result[1]

        # End Condition
        if result[2]:
            break

    env.close()
    print("Game " + str(gameNum) + " complete, final score: " + str(score))
    results[gameNum] = score


if __name__ == '__main__':

    games = []

    manager = multiprocessing.Manager()
    results = manager.dict()

    for i in range(NUM_GAMES):
        p = multiprocessing.Process(target=runGame, args=(i,results,))
        p.start()
        games.append(p)

    for i in range(NUM_GAMES):
        games[i].join()

    print("All games complete")

    print(results.values())
    highscore = max(results.values())
    print("High Score: " + str(highscore))


