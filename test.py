import gym
import multiprocessing
import time

# Change these as you'd like
RENDER_GAME = True
NUM_GAMES = 1

def runGame(gameNum, results):
    env = gym.make('MsPacman-v0')
    score = 0
    env.reset()  # New game
    print("Starting game " + str(gameNum))

    for k in range(10000):

        action = env.action_space.sample()  # This we'll want to change to a number. See: https://github.com/openai/gym/blob/master/gym/envs/atari/atari_env.py
        while action not in [0, 2, 3, 4, 5]:  # In order: no operation, up, right, left, down. This link makes it seem like diagonals would work but I don't see the point: https://github.com/mgbellemare/Arcade-Learning-Environment/blob/master/src/games/supported/MsPacman.cpp
            action = env.action_space.sample()
        result = env.step(action)  # Run the emulation through one "step" (appears to be 1 frame) and get back data about it. See: https://github.com/openai/gym/blob/master/gym/core.py

        # result = Simple array with observation (obj), reward (float), done (bool), info (dict)
        # observation seems to be an x * y * z array of row, column, and rgb pixel values. This will be what the AI reads into a tensor I'd imagine
        # reward we'll want to tweak before handing to the AI. stuff like if action in [2,3,4,5] then reward - 1 or something. perhaps life dropping should be negative 1000 or something like that too.
        # info is just {'ale.lives': int}, with int starting at 3 and dropping to 0. 

        #print(env.render(mode='rgb_array'))  # same thing as result[0] (observation)
        if RENDER_GAME:
            env.render()  # Makes a window that shows the game
            print("Iteration " + str(k) + ", Action: " + str(action) + ", Current Score: " + str(score))

        score = score + result[1]  # result[1] is the amount of increase in score from the last step

        # End Condition
        if result[2]:  # set to True once all lives are used up and ms pacman dies
            break

    env.close()  #
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


