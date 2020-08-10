# pip3 install gym
# pip3 install gym[atari]
# sudo apt install python3-opengl

import gym
import multiprocessing

# Change these as you'd like
RENDER_GAME = False
NUM_GAMES = 10

def runGame(gameNum, pipe):
    env = gym.make('MsPacman-v0')
    score = 0
    print(env)
    env.reset()
    for k in range(10000):
        #print(env.render(mode='rgb_array'))
        if RENDER_GAME:
            env.render()
        action = env.action_space.sample()
        while action not in [0, 2, 3, 4, 5]:
            action = env.action_space.sample()
        result = env.step(action) # take a random action
        print("Iteration " + str(k) + ", Action: " + str(action) + ", Current Score: " + str(score))
        #print(result)
        #print(result.observation)
        #print(result.reward)
        #print(result.done)
        #print(result.info)
        #print(result[0])
        
        score = score + result[1]

        if result[1] > 0:
            print(result[1])

        if result[2] == True:
            break

    env.close()
    print("Game " + str(gameNum) + " complete, final score: " + str(score))
    pipe.send(score)

if __name__ == '__main__':
    games = []
    pipes = []
    for i in range(NUM_GAMES):
        recv_end, send_end = multiprocessing.Pipe(False)
        p = multiprocessing.Process(target=runGame, args=(i,send_end,))
        p.start()
        games.append(p)
        pipes.append(recv_end)

    for i in range(NUM_GAMES):
        games[i].join()

    results = [x.recv() for x in pipes]
    highscore = max(r for r in results)
    print("High Score: " + str(highscore))


