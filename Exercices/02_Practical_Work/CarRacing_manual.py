#!/usr/bin/env python3

# Try to play by yourself!
from gym.envs.box2d.car_racing import *
bool_do_not_quit = True  # Boolean to quit pyglet
from pyglet.window import key
a = np.array( [0.0, 0.0, 0.0] )

def key_press(k, mod):
    global bool_do_not_quit, a, restart
    if k==0xff0d: restart = True
    if k==key.ESCAPE: bool_do_not_quit=False  # To Quit
    if k==key.Q: bool_do_not_quit=False  # To Quit
    if k==key.LEFT:  a[0] = -1.0
    if k==key.RIGHT: a[0] = +1.0
    if k==key.UP:    a[1] = +1.0
    if k==key.DOWN:  a[2] = +0.8   # set 1.0 for wheels to block to zero rotation

def key_release(k, mod):
    global a
    if k==key.LEFT  and a[0]==-1.0: a[0] = 0
    if k==key.RIGHT and a[0]==+1.0: a[0] = 0
    if k==key.UP:    a[1] = 0
    if k==key.DOWN:  a[2] = 0
env = CarRacing()
# env.render()
record_video = False  # Your can record your run if you want!
if record_video:
    env.monitor.start('/tmp/video-test', force=True)
env.reset()
env.viewer.window.on_key_press = key_press
env.viewer.window.on_key_release = key_release

while bool_do_not_quit:
    total_reward = 0.0
    steps = 0
    restart = False
    while bool_do_not_quit:
        s, r, done, info = env.step(a)
        env.render()
        total_reward += r
        if steps % 200 == 0 or done:
            print("Step: {} | Reward: {:+0.2f}".format(steps, total_reward), "| Action:", a)
        steps += 1
        if not record_video: # Faster, but you can as well call env.render() every time to play full window.
            env.render()
        if done or restart: break
env.close()

# We could also run car_racing.py but it would not quit properly:
# import subprocess
# subprocess.call(['python3', car_racing.__file__])