from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password, check_password
from django.db.models import Q
from bus.models import Bus, Station, Message, Line

from django.shortcuts import redirect


# Create your views here.


# 默认显示登录界面进入其它界面则登录
def index(request):
    return render(request, 'index.html')


# 注册账号,注册之后会自动登
def regist(request):
    if request.method == 'GET':
        return render(request, 'regist.html')
    if request.method == 'POST':
        try:
            if User.objects.get(username=request.POST.get('account')):
                return render(request, 'regist.html', {'mes': '账号已经存在，请登录或者更改注册账号!'})
        except:
            if len(request.POST.get('account')) < 6 or len(request.POST.get('password')) < 6:
                return render(request, 'regist.html', {'mes': '账号密码长度不能小于6!'})
            elif request.POST.get('password') == request.POST.get('password_2'):
                # print(len(request.POST.get('account')))
                u = User(username=request.POST.get('account'), password=make_password(request.POST.get('password')))
                u.save()
                login(request, u)
                return render(request, 'index.html')
            else:
                return render(request, 'regist.html', {'mes': '两次输入密码不一致!'})


# 登录系统
def log(request):
    try:
        u = User.objects.get(username=request.POST.get('account'))
        if check_password(request.POST.get('password'), u.password):
            if u.is_superuser:
                return redirect('admin/')
            else:
                return render(request, 'main.html', {'u': u})
        else:
            return render(request, 'index.html', {'mes': '密码错误!'})
    except:
        return render(request, 'index.html', {'mes': '用户不存在!'})


@login_required
def bus_now(request):
    return render(request, 'bus_now.html')


# 查询某线路或者名称或者某一站结果
@login_required
def search(request):
    text = request.POST.get('text')

    try:
        li = [i.bus.id for i in Station.objects.filter(Q(name__icontains=text))]
        result = Line.objects.filter(Q(id__in=li) | Q(country__icontains=text) | Q(name__icontains=text))
        if len(result) == 0:
            return render(request, 'message.html', {'mes': '未找到相关公交线路!'})
        else:
            return render(request, 'result.html', {'result': result})
    except:
        result = Line.objects.filter(Q(country__icontains=text) | Q(name__icontains=text))
        if len(result) == 0:
            return render(request, 'message.html', {'mes': '未找到相关公交线路!'})
        else:
            return render(request, 'result.html', {'result': result})


@login_required
def st(request, id):
    result = Station.objects.filter(bus=id).order_by('number')
    if bus_at(id, True) == False or bus_at(id, True) == None:
        return render(request, 'st.html', {'result': result, 'id': id, 'mes': '公交车未在运行时间段内或等待管理员添加公交车！'})
    else:
        dict, data = bus_at(id, True)
        return render(request, 'st.html', {'result': result, 'id': id, 'dict': dict, 'data': data})


@login_required
def sc(request, id):
    result = Station.objects.filter(bus=id).order_by('-number')
    if bus_at(id, False) == False or bus_at(id, False) == None:
        return render(request, 'sc.html', {'result': result, 'id': id, 'mes': '公交车未在运行时间段内或等待管理员添加公交车！'})
    else:
        dict, data = bus_at(id, False)
        return render(request, 'sc.html', {'result': result, 'id': id, 'dict': dict, 'data': data})


# @login_required
def bus_at(id, direction):
    # try:
    import datetime
    time_now = datetime.datetime.now()
    result = Line.objects.get(id=id)
    dict = {}
    dict['线路名称'] = result.name
    dict['票价'] = str(result.money)+'元'
    # 判断当前时间是否为运行时间
    if result.start <= time_now.hour < result.end:
        # 获取运行时间
        bus_run = time_now.hour * 60 + time_now.minute - result.start * 60
        # bus_run = 20
        # 所有站点

        all_sta = len(Station.objects.filter(bus=result.id))
	# 加这一行
	#stas = Station.objects.filter(bus=result.id)
        
	# 单程线路时间
        run_time = all_sta * result.need
        # 一辆公交车运行总时间
        bus_run_time = run_time * 2
        # 单程线路所需公交车数量
        count = run_time // result.count + 1
        # 线路公交车数辆
        buss = Bus.objects.filter(line=result.id)
        if len(buss) < 2:
            return False
        else:
            # 分为去程和返程
            bus = len(buss) // 2
            num = None
            # 运行时间未超过发车时间
            if bus_run < result.count:
                num = 1
            # 公交车总数小于线路所需公交车熟辆
            elif bus < count:
                num = bus
            else:
                num = count
            res = []
            for i in range(0, num + 1, 2):
                data = {}
                array_time = result.need - bus_run % bus_run_time % result.need
                car = None
                sta = None
                next_sta = None
                # 方向
                if direction == True:
                    if bus_run % bus_run_time // result.need > all_sta:
                        car = buss[i + 1]
                        sta = Station.objects.filter(id=id).get(number=bus_run % bus_run_time // result.need - all_sta)
                    else:
                        car = buss[i]
                        if bus_run % bus_run_time // result.need == all_sta:
                            sta = Station.objects.filter(id=id).get(number=bus_run % bus_run_time // result.need)
                        else:
                            sta = Station.objects.filter(id=id).get(number=bus_run % bus_run_time // result.need + 1)
                    if sta.number < all_sta:
                        next_sta = Station.objects.filter(id=id).get(number=sta.number + 1).name

                else:
                    if bus_run % bus_run_time // result.need > all_sta:
                        car = buss[i]
                        sta = Station.objects.filter(id=id).get(number=bus_run % bus_run_time // result.need - all_sta)
                    else:
                        car = buss[i + 1]
                        if bus_run % bus_run_time // result.need == all_sta:
                            sta = Station.objects.filter(id=id).get(number=bus_run % bus_run_time // result.need)
                        else:
                            sta = Station.objects.filter(id=id).get(number=all_sta - bus_run % bus_run_time // result.need)
                    if sta.number <= all_sta:
                        next_sta = Station.objects.filter(id=id).get(number=sta.number - 1).name
                # print(car, array_time, sta, next_sta)
                data['car'] = car
                data['array_time'] = array_time
                data['sta'] = sta.name
                data['next_sta'] = next_sta
                res.append(data)
                bus_run -= result.count
        return dict, res
    else:
        return None


@login_required
def comment(request, id):
    # if request.method == 'GET':
    com = Message.objects.all().order_by('-add_date')
    return render(request, 'comment.html', {'com': com, 'id': id})


@login_required
def ct(request, id):
    # elif request.method == 'POST':
    comm = request.POST.get('content')
    user = User.objects.get(id=id)
    c = Message(user=user, content=comm)
    c.save()
    return redirect('/comment/' + str(id))
