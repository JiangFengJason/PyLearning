import numpy as np
import pandas as pd
import time

np.random.seed(2)

N_STATE = 6 #状态的数目
ACTIONS = ['left','right'] #可选择的动作范围
EPSILON = 0.9 #选择动作的贪心值
ALPHA = 0.1 #学习速率
LAMBDA = 0.9 #未来奖励值大小
MAX_EPISODES = 13 #最大的学习回合数
FRESH_TIME = 0.3 #走一步花的时间长度

def build_q_table(n_state,actions):
    table = pd.DataFrame(
        np.zeros((n_state,len(actions))),
        columns=actions,
    )
    #print(table)
    return table

def choose_action(state,q_table):
    