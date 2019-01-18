# Created by Helic on 2017/10/21
from DialogManager.DialogManager import DM

dm = DM()
flag = True
# 开场白
print("agent: 您好，学科英语首创品牌“瑞思学科英语”欢迎您，本月免费试听中，名额有限！留下姓名及联系方式马上获取试听机会！抢约：400-610-1100")
while flag:
    usr_raw_sentence = input("user: ")
    agent_response_diaact, index = dm.agent_response(usr_raw_sentence)
    print("agent_diaact:", agent_response_diaact, '\n', "index: ", index)
    agent_nl = dm.agent_nl(agent_response_diaact, index)
    print("agent: ", agent_nl)
    flag = not dm.flag
print(dm.agent_inform_slots)
# dm.update_database()




