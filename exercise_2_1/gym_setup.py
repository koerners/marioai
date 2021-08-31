import subprocess

import gym
import gym_marioai

# reward function params
prog = 2
timestep = -1
mario_mode = 0
cliff = 0
kill = 0
coin = 0
win = 150
dead = -10

reward_settings = gym_marioai.RewardSettings(progress=prog, timestep=timestep, mario_mode=mario_mode, kill=kill,
                                             coin=coin, win=win, dead=dead, cliff=cliff)


class Env:
    def open(self, port):
        return subprocess.Popen(['java', '-jar', 'server.jar', '-p', str(port)])

    def __init__(self, visible=True, port=8080, level='None', run_server=True):
        if run_server:
            self.server = self.open(port)
        self.all_actions = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
        self.env = gym.make('Marioai-v0', render=visible,
                            level_path=level,
                            compact_observation=False,
                            reward_settings=reward_settings,
                            enabled_actions=self.all_actions,
                            rf_width=20, rf_height=10,
                            port=port)
