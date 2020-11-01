# 导入需要的python包
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import vthread

# 读取数据
pot_data = pd.read_csv('数据集/景点.csv')
user_data = pd.read_csv('数据集/用户访问.csv')
comment_data = pd.read_csv('数据集/用户评论.csv')
user = pd.read_csv('数据集/用户评论.csv')['用户名']

# plt.rcParams["font.sans-serif"]=['SimHei']  


# 求平均数方法
def get_average(li):
    from collections import Counter    
    score = []
    comment = []
    new_cls = []
    for i in li:
        try:
            score.append(float(list(pot_data[pot_data['景点名称']==i]['评分'])[0]))
            comment.append(int(list(pot_data[pot_data['景点名称']==i]['评论数'])[0]))
        except:
            continue
        new_cls.append(list(pot_data[pot_data['景点名称']==i]['新分类'])[0])
    new_score = dict(Counter(score))
    
    for k,v in new_score.items():
        new_score[k] = round(v/len(score)*100,2)
    
    return [round(sum(score)/len(score),2),round(sum(comment)/len(comment),2),sorted(dict(Counter(new_cls)).items(),key=lambda x: x[0]),new_score]



# @vthread.pool(8)
def plot_one():
    import os
    # 判断是否存在重复景点文件，如果不存在从数据中筛选
    if not os.path.exists('repeat.txt'):

        # 循环所有用户，在用户访问中获取记录
        # 定义一个重复景点列表
        from collections import Counter    
        repeat_pot = []
        #取出每个用户名循环便利从中取出重复的景点名称
        for i in list(set(user)):
            pot = user_data[user_data['用户名']==i]['景点名']
            # 通过counter列表计数方法取出大于一的重复景点
            repeat_pot += [k for k,v in dict(Counter(list(pot))).items() if int(v) > 1]
        with open('repeat.txt','w') as f:
            f.write(','.join(repeat_pot)) 
    #获得重复景点和非重复景点
    repeat_pot = open('repeat.txt').read().split(',')
    all_pot = list(pot_data['景点名称'])
    not_repeat = list(set(all_pot) - set(repeat_pot))
    # repeat_data = pd.DataFrame(columns=pot_data.columns)
    # for i in repeat_pot:
        # repeat_data.append(pot_data[pot_data['景点名称']==i])
    # repeat_data.to_csv('repeat.csv')
    # Nrepeat_data = pd.DataFrame(columns=pot_data.columns)
    # for i in not_repeat:
        # Nrepeat_data.append(pot_data[pot_data['景点名称']==i])
    # Nrepeat_data.to_csv('Nrepeat.csv')
    # 查询景点
    repeat_result = get_average(repeat_pot)
    Nrepeat_result = get_average(not_repeat)
    return repeat_result,Nrepeat_result

   
    
# 第二个问题处理
# @vthread.pool(8)
def plot_that():
    all_comment = {}
    #取出所有用户和评论做排序
    for i in (list(set(user))):
        all_comment[i] = list(comment_data[comment_data['用户名']==i]['收获到的点赞数'])[0]
    sort_comment = sorted(all_comment.items(),key=lambda all_comment: all_comment[1],reverse=True)
    # 获得网红游客
    tuorist_user = [i[0] for i in sort_comment[:int(len(sort_comment)*0.2)]]
    Ntuorist_user = [i[0] for i in sort_comment[int(len(sort_comment)*0.2):]]
    # 从网红游客中获取景点
    tuorist_pot = []
    # tuorist_data = pd.DataFrame(columns=user_data.columns)
    for i in tuorist_user:
        tuorist_pot += list(user_data[user_data['用户名']==i]['景点名'])
        # tuorist_data = tuorist_data.append(pd.DataFrame(user_data[user_data['用户名']==i],columns=tuorist_data.columns))

    # tuorist_data.to_csv('Celebirty.csv')

    tuorist_pot = list(set(tuorist_pot))
    Ntuorist_pot = []
    # N_tuorist = pd.DataFrame(columns=user_data.columns)
    for i in Ntuorist_user:
        Ntuorist_pot += list(user_data[user_data['用户名']==i]['景点名'])
        # N_tuorist = N_tuorist.append(pd.DataFrame(user_data[user_data['用户名']==i]))
    # N_tuorist.to_csv('average_people.csv')
    Ntuorist_pot = list(set(Ntuorist_pot))
    tuorist_result = get_average(tuorist_pot)
    Ntuorist_result = get_average(Ntuorist_pot)
    return tuorist_result,Ntuorist_result

    
def plot(repeat_result,Nrepeat_result,name):
    # 第一个评分评论数对比图
    name_list = [name[0]+'score',name[1]+'score',name[0]+'comment',name[1]+'comment']
    ax = plt.subplot(221)
    width = 0.5
    rects = ax.bar(range(0,4),[repeat_result[0],Nrepeat_result[0],repeat_result[1],Nrepeat_result[1]],color='rgb',tick_label=name_list,width=width)
    ax.set_title('avarage score and comment')
    ax.set_ylabel('average_number')
    ax.set_xlabel('cls')
    for rect in rects:
        x = rect.get_x()
        height = rect.get_height()
        ax.text(x+0.2,1.01*height,str(height))
    
    # 第二个
    bx = plt.subplot(222)
    a = sorted(repeat_result[-1].items(),key=lambda x:x[0])
    b = sorted(Nrepeat_result[-1].items())
    x1 = [k[0] for k in a ]
    y1 = [k[1] for k in a]
    x2 = [i[0] for i in b]
    y2 = [i[1] for i in b]
    cls_1, = bx.plot(x1,y1,'r',label='cls_1')
    cls_2, = bx.plot(x2,y2,'g',label='cls_2')
    # bx.plot(x1,y1,'ro-',x2,y2,'g+-')
    bx.set_title('score')
    bx.set_xlabel('score')
    bx.set_ylabel('percentage')
    plt.legend([cls_1,cls_2],[name[0],name[1]])

    ax1 = plt.subplot(223)
    ax1.set_title(name[0])
    # plt.figure(figsize=(10,15))
    labels = [k[0] for k in repeat_result[2]]
    sizes = [v[1] for v in repeat_result[2]]
    colors = ['red','yellow','blue','lightskyblue','yellowgreen']
    explode = tuple([0 for i in range(0,len(sizes))])
    patches,text1,text2 = ax1.pie(sizes,explode=explode,labels=labels,colors=colors,autopct='%3.2f',shadow=False,startangle=90,pctdistance=0.9)
    ax1.axis('equal')
    ax2 = plt.subplot(224)
    ax2.set_title(name[1])
    Nlabels = [k[0] for k in Nrepeat_result[2]]
    Nsizes = [v[1] for v in Nrepeat_result[2]]
    pathes, text3,text4 = ax2.pie(Nsizes,explode=explode,labels=Nlabels,colors=colors,autopct='%3.2f',shadow=False,startangle=90,pctdistance=0.9)
    ax2.axis('equal')
    plt.show()

# @vthread.pool(3)
def main():
    repeat_data,Nrepeat_data=plot_one()
    # tuorist_data,Ntuorist_data = plot_that()
    # plot(repeat_data,Nrepeat_data,name=['Repeated','Non_Repeated'])
    # plot(tuorist_data,Nrepeat_data,name=['Celebrity','average_people'])



if __name__ == '__main__':
    main()
    # plt.show()