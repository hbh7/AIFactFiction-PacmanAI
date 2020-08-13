# pip3 install gym
# pip3 install gym[atari]
# sudo apt install python3-opengl

import gym
import multiprocessing
import time

# Change these as you'd like
RENDER_GAME = True
NUM_GAMES = 1
CUSTOM_SCORING = False
VERBOSE_PRINTOUT = True

# Custom scoring settings
NO_SCORE_LIMIT = 87 # Number of frames without getting any points before points are deducted
TIME_LIMIT = 2900 # Number of frames in a fast play of level 1; if passed, points are deducted
FRAMES_PER_POINT = 60 # Number of frames that pass before 10 points are deducted

def runGame(gameNum, results):
    env = gym.make('MsPacman-v0')
    score = 0
    env.reset()  # New game
    print("Starting game " + str(gameNum))

    # For custom scoring
    custom_score = 0
    lastTimeScored = 0 # Last frame that points were added.
    lastTimeDeducted = 0 # Last frame that points was deducted.

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
        if CUSTOM_SCORING:
            if result[1] > 0:
                custom_score = custom_score + result[1]
                lastTimeScored = k
            else:
                if k - lastTimeScored >= lastTimeScored:
                    if k - lastTimeDeducted >= FRAMES_PER_POINT:
                        lastTimeDeducted = k
                        custom_score = custom_score - 10
            if k > TIME_LIMIT:
                if k - lastTimeDeducted >= FRAMES_PER_POINT:
                    lastTimeDeducted = k
                    custom_score = custom_score - 10
            

        # End Condition
        if result[2]:  # set to True once all lives are used up and ms pacman dies
            break

    env.close()  #
    print("Game " + str(gameNum) + " complete, final score: " + str(score))
    if CUSTOM_SCORING:
        print("Custom score for game " + str(gameNum) + ": " + str(custom_score))

    results[gameNum] = {
        'game' : gameNum,
        'score' : score,
        'custom_score' : custom_score,
        'moves' : k
    }


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

    if VERBOSE_PRINTOUT:
        # Print a detailed version of the results, including number of moves, score, and if custom scoring is on,
        # custom score.
        highscoring_game = max(results.values(), key=lambda item: item['score'])
        print("Highest Scoring Game: Game " + str(highscoring_game['game']))
        print("\tNumber of Moves: " + str(highscoring_game['moves']))
        print("\tScore: " + str(highscoring_game['score']))
        if CUSTOM_SCORING:
            print("\tCustom Score: " + str(highscoring_game['custom_score']))
            custom_highscoring_game = max(results.values(), key=lambda item: item['custom_score'])
            print("Highest Custom Scoring Game: Game " + str(custom_highscoring_game['game']))
            print("\tNumber of Moves: " + str(custom_highscoring_game['moves']))
            print("\tScore: " + str(custom_highscoring_game['score']))
            print("\tCustom Score: " + str(custom_highscoring_game['custom_score']))
        lowscoring_game = min(results.values(), key=lambda item: item['score'])
        print("Lowest Scoring Game: Game " + str(lowscoring_game['game']))
        print("\tNumber of Moves: " + str(lowscoring_game['moves']))
        print("\tScore: " + str(lowscoring_game['score']))
        if CUSTOM_SCORING:
            print("\tCustom Score: " + str(lowscoring_game['custom_score']))
            custom_lowscoring_game = min(results.values(), key=lambda item: item['custom_score'])
            print("Lowest Custom Scoring Game: Game " + str(custom_lowscoring_game['game']))
            print("\tNumber of Moves: " + str(custom_lowscoring_game['moves']))
            print("\tScore: " + str(custom_lowscoring_game['score']))
            print("\tCustom Score: " + str(custom_lowscoring_game['custom_score']))
    else:
        # Print a basic version of the results, just including the score, and if custom score is on, the custom score.
        highscoring_game = max(results.values(), key=lambda item: item['score'])
        lowscoring_game = min(results.values(), key=lambda item: item['score'])
        print("Highest Scoring Game: Game " + str(highscoring_game['game']) + ", Score: " + str(highscoring_game['score']))
        if CUSTOM_SCORING:
            custom_highscoring_game = max(results.values(), key=lambda item: item['custom_score'])
            print("Highest Custom Scoring Game: Game " + str(custom_highscoring_game['game']) + ", Score: " + str(custom_highscoring_game['custom_score']))
        print("Lowest Scoring Game: Game " + str(lowscoring_game['game']) + ", Score: " + str(lowscoring_game['score']))
        if CUSTOM_SCORING:
            custom_lowscoring_game = min(results.values(), key=lambda item: item['custom_score'])
            print("Lowest Custom Scoring Game: Game " + str(custom_lowscoring_game['game']) + ", Score: " + str(custom_lowscoring_game['custom_score']))

