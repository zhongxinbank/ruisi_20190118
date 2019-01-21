# Created by Helic on 2017/10/21
from DialogManager.DialogManager import DM

dm = DM()
flag = True
# 开场白
print("agent: 您好，学科英语首创品牌“瑞思学科英语”欢迎您，本月免费试听中，名额有限！留下姓名及联系方式马上获取试听机会！抢约：400-610-1100")
while flag:
    usr_raw_sentence = input("user: ")
    agent_response_diaact, index = dm.agent_response(usr_raw_sentence)
    try:
        agent_nl = dm.agent_nl(agent_response_diaact, index)
    except KeyError as e:
        agent_nl = "家长可以留下您的联系方式哦，我们后续会安排专业的老师与您对接，为您详细介绍相关事宜。"
    print("agent: ", agent_nl)
    flag = not dm.flag
    note = dm.get_database() # 要存入文件的string
    print(note)
# dm.update_database()




