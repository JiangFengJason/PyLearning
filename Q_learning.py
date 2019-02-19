import numpy as np
import pandas as pd
import time

np.random.seed(2)

N_STATE = 6 #状态的数目
ACTIONS = ['left','right'] #可选择的动作范围
EPSILON = 0.9 #选择动作的贪心值
ALPHA = 0.1 #学习速率
LAMBDA = 0.9 #未来奖励值大小
MAX_EPISODES = 15 #最大的学习回合数
FRESH_TIME = 0.1 #走一步花的时间长度

def build_q_table(n_state,actions):
    table = pd.DataFrame(
        np.zeros((n_state,len(actions))),
        columns=actions,
    )
    #print(table)
    return table

def choose_action(state,q_table):
    state_actions=q_table.iloc[state,:]
    #如果全零或者大于0.9那么就选择随机动作
    if (np.random.uniform()>EPSILON) or (state_actions.all()==0):
        action_name=np.random.choice(ACTIONS)
    #否则选择动作值中最大的那个值
    else :
        action_name=state_actions.argmax()
    return action_name

def get_env_feedback(S,A):
    if A=='right':
        if S==N_STATE-2:
            R=1 #到达终点
            S_='terminal'
        else :
            R=0
            S_=S+1
    else:
        R=0
        if S==0:
            S_=S #撞墙了
        else :
            S_=S-1
    return S_,R

def update_env(S,episode,step_counter):##环境更新重新绘制，可以选择性不看
    env_list=['-']*(N_STATE-1)+['T']
    if S=='terminal':
        interaction='Episode %s : total_step = %s' % (episode+1,step_counter)
        print ('\r{}'.format(interaction),end='')
        time.sleep(2)
        print ('\r                               ',end='')
    else :
        env_list[S]='o'
        interaction=''.join(env_list)
        print('\r{}'.format(interaction),end='')
        time.sleep(FRESH_TIME)

def rl():
    q_table=build_q_table(N_STATE,ACTIONS)
    for episode in range(MAX_EPISODES):
        step_counter=0
        S=0
        is_terminated=False
        update_env(S,episode,step_counter)
        while not is_terminated:
            A=choose_action(S,q_table)
            S_,R = get_env_feedback(S,A)
            q_predict=q_table.loc[S,A]
            if S_ != 'terminal':
                q_target=R+LAMBDA*q_table.iloc[S_,:].max()
            else :
                q_target=R
                is_terminated=True
            
            q_table.loc[S,A]+=ALPHA*(q_target - q_predict)
            S=S_

            update_env(S,episode,step_counter+1)
            step_counter+=1
    return q_table

#if _name_=='_main_':
q_table=rl()
print ('\r\nQ-table:\n')
print (q_table)