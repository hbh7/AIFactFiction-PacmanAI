# AIFactFiction-PacmanAI

## To-Do List

- [ ] Write Model
  - Based on / assisted by Microsoft analysis  
  - v0.1 by EOD 14/06/2020
  - Ivan?
  
- [ ] Write Reward Function
  - Points from game ( given by OpenAIGym ) + game rule edits
  - Will?
  
- [ ] Write Training Function
  - Rewrite Lab04 code ( reward / accuracy difference? )
  - Pytorch documentation reading
  
- [ ] Write Game Integration Function
  - Use model to play game ( run model on input and use chosen ouptut move as PacMan move )
  - Loop: Run model on frame -> use model's output move as input -> next frame
  - Hunter?
  
- [ ] Write Train->Play->Train->Play->... Loop
  - Simple loop of Training Function and Game Integration Function
  - As model improves more games, more data, longer training runs (reinforcement learning)
  
- [ ] Write save-load protocol
  - Mostly documentation reading, simple implementation


## Setup instructions

### WSL2 (Preferred)

Adapted from https://medium.com/swlh/get-wsl2-working-on-windows-10-2ee84ef8ed43

1. Set up and install WSL2 according to the directions from Microsoft. WSL2 is required I believe as WSL 1 doesn't have necessary functions or something.

2. Install VcXsrv from https://sourceforge.net/projects/vcxsrv/

3. Install PuTTY

4. Run VcXsrv (likely XLaunch in Windows Start Menu), click next through settings. 

5. Run these commands in WSL: 
    ```
    sudo apt-get remove --purge openssh-server
    sudo apt-get update
    sudo apt-get upgrade -y
    sudo apt-get install -y openssh-server
    ```

6. Edit the SSH server config with `nano /etc/ssh/sshd_config`

7. Make sure the following lines are uncommented/set:
    ```
    X11Forwarding yes
    X11DisplayOffset 10
    ```

8. Run: `sudo service ssh restart`

9. Open PuTTY, go to `Connection` -> `SSH` -> `X11` and check `Enable X11 forwarding` and set the `X display location` to `127.0.0.1:0.0`.

10. Return to the `Session` tab. Enter `localhost` as the `Host Name`, or optionally (for convenience) add your username, like `username@localhost`.

11. Also for convenience, type a name in `Saved Sessions` like `WSL Local SSH` or something, and press save. This makes it so you don't have to configure PuTTY every time, you can just double click the entry in the sessions list. 

12. Press open (or double click the session you made) and log in with your WSL username/password.

13. Change to the code directory using the `cd` command. This will probably be something like `cd /mnt/c/Users/yourname/Documents/Github/AIFactFiction-PacmanAI`. 

14. Install dependencies:
    ```
    sudo apt install python3 python3-pip python3-opengl
    sudo pip3 install gym
    sudo pip3 install gym[atari]
    ```

15. Run the code with `python3 filename.py`.

16. You should now have success! Hopefully anyways