
import pandas as pd
import math
import time
import numpy as np
import matplotlib.pyplot as plt 

# 读取数据


pot_data = pd.read_csv('数据集/景点.csv')
user_data = pd.read_csv('数据集/用户访问.csv',na_values='2019年1月')
comment_data = pd.read_csv('数据集/用户评论.csv')
user = pd.read_csv('数据集/用户评论.csv')['用户名']



# 访问频率
def get_sf(data,pot_cls):
    # 去过的所有景点
    post_all = data
    # 景点类别
    clss = [list(pot_data[pot_data['景点名称']==i]['新分类'])[0] for i in post_all]
    try:
        sf = math.exp(-(clss.count(pot_cls)/len(clss)))
    except:
        sf = math.exp(-0)
    return sf




# 时间新颖度
def get_sr(data,pot_cls):
    # 上次访问该类别的时间
    try:

        post_all = data
        clss = [list(pot_data[pot_data['景点名称']==i]['新分类'])[0] for i in post_all]
        pot = post_all[max([clss.index(i) for i in clss if i==pot_cls])]
        last_time = list(data[data['景点名']==pot]['旅游日期'])[0]
        if '#'  in last_time:
            last_time = '2019年1月'
        a = []
        for i in last_time:
            if i == '年' or i== '月':
                a.append(last_time.index(i))
        year = last_time[:a[0]]
        moth = last_time[a[0]+1:a[1]]
        import datetime
        now_year = datetime.datetime.now().year
        now_moth = datetime.datetime.now().month
        if now_year >= int(year):
            t = (now_year-int(year))*12+(now_moth-int(moth))
        else:
            t = now_moth - int(moth)
    except:
        t = 0
    sr = 1-math.exp(-(0.1*t))
    return sr



# 频率新颖度加时间新颖度
def get_xin(data,pro_cls):
    value = 0.5*(get_sf(data,pro_cls)+get_sr(data,pro_cls))
    return value



# 获取全部用户
def get_all_score():
    # 取出所有用户,目前取十个
    u = list(set(user))[:10]
    all_result = []
    for i in u:
        all_result.append(deal_every_time(i))
    ar = np.array(all_result)
    result = np.mean(ar,axis=0).tolist()
    return result


# 处理新颖度到百分比
def plot(value):
    p = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0]    
    a = len([i for i in value if i<=0.1])/len(value)
    b = len([i for i in value if 0.1<i<=0.2])/len(value)
    c = len([i for i in value if 0.2<i<=0.3])/len(value)
    d = len([i for i in value if 0.3<i<=0.4])/len(value)
    e = len([i for i in value if 0.4<i<=0.5])/len(value)
    f = len([i for i in value if 0.5<i<=0.6])/len(value)
    g = len([i for i in value if 0.6<i<=0.7])/len(value)
    h = len([i for i in value if 0.7<i<=0.8])/len(value)
    i = len([i for i in value if 0.8<i<=0.9])/len(value)
    j = len([i for i in value if 0.9<i])/len(value)
    x = [a,b,c,d,e,f,g,h,i,j]
    return p,x


def sort_data(username):
    dic = {}
    data = user_data[user_data['用户名']==username]
    for i,row in data.iterrows():
        dic[row['景点名']] = row['旅游日期']
        print(row['景点名'],row['旅游日期'])
    result = sorted(dic.items(),key=lambda  k: k[1])
    return result

def rep_time(l):
    r = l.replace('年',' ').replace('月','')
    a = r.split(' ')
    return int(a[0])*12+int(a[1])


# 根据时间点划分
def deal_every_time(username):
    res = sort_data(username)
    value = []
    for i in list(sorted(set(list([i[1] for i in res])))):
        
        if '#'  in i:
            i = '2019年1月'
        a = []
        for j in res:
            if '#'  in j[1]:
                j[1] = '2019年1月'
            if rep_time(i) >= rep_time(j[1]):
                a.append(j[0])
        value.append(a)
    data = []
    for k in value:
        pro_cls=['a1','a2','a3','a4','a5','a6','a7','a8','a9']
        e = []
        for j in pro_cls:
            e.append(get_xin(k,j))
        data.append(e)
    # 默认返回最终结果请在此修改
    return data[max([data.index(i) for i in data])]


# 画出用户平均
def plot_all():
    p,x = plot(get_all_score())
    plt.figure(figsize=(16,8))
    plt.bar(p,x,tick_label=p,width=0.05)   
    plt.plot(p,x,'ro--')
    plt.savefig('all_user.png')



# 获取单个用户     除了新颖度百分比之外还有归一化
def plot_one_score(username):
    result = deal_every_time(username)
    p,x = plot(result)
    import os
    os.mkdir(username)
    plt.figure(figsize=(16,8))
    plt.bar(p,x,tick_label=p,width=0.05)   
    plt.plot(p,x,'ro--')
    plt.savefig(username+'/'+'user_all.png')
    
    x = [i/max(x) for i in x]
    plt.figure(figsize=(16,8))
    plt.plot(p,x,'ro--')
    plt.savefig(username+'/'+username+'.png')

# 画出单个用户实例   
# plot_all()
plot_one_score('鶴田 直己')
