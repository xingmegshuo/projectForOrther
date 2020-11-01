from django.shortcuts import render, redirect

# Create your views here.


from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.views.generic.list import ListView
from ZpModel.models import Com, Zp, CV, Relation
from django.forms.models import model_to_dict


def register(request):
    context = {}
    return render(request, 'register.html', context)


def logIN(request):
    username = request.GET.get('username')
    password = request.GET.get('password')
    try:
        user = User.objects.get(username=username)
    except:
        return HttpResponse("用户不存在！")
    if check_password(password, user.password):
        login(request, user)
        return HttpResponse("登录成功")
    else:
        return HttpResponse("密码错误！")


def logOUT(request):
    logout(request)
    return HttpResponse(str(request.POST))


def reg(request):
    name = request.GET.get('name')
    username = request.GET.get('username')
    password = request.GET.get('password')
    email = request.GET.get('email')
    type = request.GET.get('type')
    if username and password:
        if len(username) < 6:
            return HttpResponse("用户账号长度小于3")
        if len(password) < 6:
            return HttpResponse("密码长度小于6")
    else:
        return HttpResponse("用户名密码为空")
    u = User(username=username, password=make_password(password), email=email, first_name=name,
             last_name=type)  # pt表示普通用户，qy表示企业用户
    try:
        u.save()
    except:
        return HttpResponse("已存在的用户名")
    login(request, u)
    return HttpResponse("注册成功")


def forgotPasswd(request):
    email = User.objects.get(username=request.user).email
    from django.core.mail import send_mail
    import random
    code = random.randint(1000, 9999)
    send_mail(
        'Subject here',
        "code is " + str(code),
        '2493603878@qq.com',
        [email],
        fail_silently=False,
    )
    return HttpResponse('您的密码已发送到您的邮件')


def changePaawd(request):
    username = request.user
    password = request.POST.get('password')
    User.objects.fiter(username=username).update(password=make_password(password))
    return HttpResponse("修改成功")


class ZpListView(ListView):
    we = ""
    edu = ""
    job = ""
    salary = ""
    path = ""
    search = ""
    user = "登录"
    model = Zp  # 数据源
    template_name = "index.html"  # 网页链接
    paginate_by = 10  # if pagination is desired，分页每页的信息条数

    # 修改查询数据
    def get_queryset(self):
        d = {"edu1": "大专", "edu2": "本科", "edu3": "硕士", "edu4": "博士", "edu5": "不限",
             "job1": "教育", "job2": "互联网", "job3": "管理", "job4": "文秘", "job5": "电子", "job6": "机械", "job7": "客服",
             "job8": "销售",
             "job9": "银行", "job10": "保险", "job11": "汽车", "job12": "采购", "job13": "化工", "job14": "设计",
             "we1": [1, 3], "we2": [3, 5], "we3": [5, 10], "we4": [10, 100],
             "sa1": [0, 3], "sa2": [3, 5], "sa3": [5, 10], "sa4": [10, 30], "sa5": [30, 1000], "sa6": [0, 0]}
        r = Zp.objects.all()
        # 搜索框
        try:
            import re
            self.search = re.match('/list_(.*)', self.path).group(1)
            # print(self.search)
            r = r.filter(jobName__contains=self.search)
        except:
            pass
        # 教育等级
        if self.edu != None and self.edu != "":
            edus = self.edu.split('_')
            eduLevel = [d[x] for x in edus if x in d.keys()]
            if len(eduLevel) == 1:
                r = r.filter(academic=eduLevel[0])
            elif len(eduLevel) == 0:
                pass
            else:
                r = r.filter(academic__in=eduLevel)
        # 工作领域
        if self.job != None and self.job != "":
            jobs = self.job.split('_')
            jobType = [d[x] for x in jobs if x in d.keys()]
            try:
                r = r.filter(reduce(operator.or_, map(lambda x: Q(jobType__contains=x), jobType)))
            except:
                pass
        # 薪资
        # if self.salary!=None and self.salary!="":
        #     k=[]
        #     for x in self.salary.split('_'):
        #         if x in d.keys():
        #             k.append(d[x])
        #     r = r.filter(reduce(operator.or_, map(lambda x: Q(K1__gte=x[0]) & Q(K2__lte=x[1]), k)))
        # #经验
        # if self.we!=None and self.we!="":
        #     k=[]
        #     for x in self.we.split('_'):
        #         if x in d.keys():
        #             k.append(d[x])
        #     r = r.filter(reduce(operator.or_, map(lambda x: Q(W1__gte=x[0]) & Q(W2__lte=x[1]), k)))
        return r

    # 添加返回数据
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.user != None and self.user != "" and not self.user.is_anonymous:
            context['user'] = '<i class="fa fa-user-circle" style="font-size:19px"></i>&nbsp' + str(self.user) + '</a>' \
                                                                                                                 '&nbsp&nbsp&nbsp<a class="text-white" id="logout"> <i class="fa fa-sign-out" style="font-size:19px"></i>注销'
        else:
            context['user'] = '<i class="fa fa-sign-in" style="font-size:19px"></i>&nbsp&nbsp<span>登录</span>'
        return context

    # 获取request
    def get(self, request, *args, **kwargs):
        self.we = request.GET.get('we')
        self.edu = request.GET.get('edu')
        self.job = request.GET.get('job')
        self.salary = request.GET.get('salary')
        self.path = request.path
        self.user = request.user
        r = super().get(self, request, *args, **kwargs)
        return r


def jl(request):
    if request.user.is_authenticated:
        u = User.objects.get(username=request.user)
        if u.last_name == 'pt':
            return HttpResponse('对不起，您不是学院用户')
        else:
            import random
            sample = [i for i in range(0, CV.objects.count())]
            if len(sample) > 10:
                sample = [random.choice(sample) for i in range(0, 10)]
            else:
                pass
            cv = [CV.objects.all()[i] for i in sample]
            return render(request, 'match_CV.html', {'cv': cv, })
    else:

        return redirect('/register')


def loginfo(request):
    user = request.user
    u = user.objects.get(username=user)
    if user != None and user != "" and not user.is_anonymous:

        context = '<i class="fa fa-user-circle" style="font-size:19px"></i>&nbsp' + str(u.first_name) + '</a>' \
                                                                                                        '&nbsp&nbsp&nbsp<a class="text-white" id="logout"> <i class="fa fa-sign-out" style="font-size:19px"></i>注销'
    else:
        context['user'] = loginfo(request)
    context = '<i class="fa fa-sign-in" style="font-size:19px"></i>&nbsp&nbsp<span>登录</span>'
    return context


def me(request):
    context = {}
    # context['user'] = loginfo(request)
    if request.user.is_authenticated:
        u = User.objects.get(username=request.user)
        if u.last_name == 'pt':

            try:
                cv = CV.objects.get(user=u)
                return redirect('http://localhost:8000' + cv.resume.url)
            except:
                return HttpResponse('请先完善个人信息')
        else:
            try:
                com = Com.objects.get(user=u)
                return render(request, 'me.html')
            except:
                return HttpResponse('请先完善个人信息')
    else:
        # 如果没有登录就返回注册
        return redirect('/register')


def create_job(request):
    com = None
    try:
        u = User.objects.get(username=request.user)
        com = Com.objects.get(user=u)
    except:
        return HttpResponse('请先完善个人信息')
    job = Zp()
    job.com = com
    job.jobName = request.POST.get('jobName')
    job.jobTitle = request.POST.get('jobTitle')
    job.number = request.POST.get('number')
    job.academic = request.POST.get('academic')
    job.pre = request.POST.get('pre')
    job.welfare = request.POST.get('welfare')
    job.need_number = request.POST.get('need_number')
    job.jobprofile = request.POST.get('jobprofile')
    job.jobType = request.POST.get('jobType')
    job.save()
    return redirect('/')


def save_info(request):
    u = User.objects.get(username=request.user)
    if u.last_name == 'pt':
        cv = None
        try:
            cv = CV.objects.get(user=u)
        except:
            cv = CV()
            cv.user = u
        cv.name = u.first_name
        cv.sex = True if request.POST.get('sex') == '男' else False
        print(len(request.POST.get('sex')))
        cv.location = request.POST.get('location')
        if request.FILES.get('myfile', None) is not None:
            cv.photo = request.FILES.get('myfile')
        if request.FILES.get('cv', None) is not None:
            cv.resume = request.FILES.get('cv')
            # import os
            # destination = open(os.path.join("media/user/", request.FILES.get('myfile').name), 'wb+')
            # destination.close()
        cv.save()
        # print(request.FILES.get('myfile').name)
    else:
        com = None
        try:
            com = Com.objects.get(user=u)
        except:
            com = Com()
            com.user = u
        com.name = u.first_name
        com.number = request.POST.get('number')
        com.Cinfo = request.POST.get('info')
        com.Companyprofile = request.POST.get('profile')
        if request.FILES.get('myfile', None) is not None:
            com.logo = request.FILES.get('myfile')
        com.save()
    return HttpResponse('个人信息完善成功')


def info(request):
    if request.user.is_authenticated:
        u = User.objects.get(username=request.user)
        l = None
        try:
            if u.last_name == 'pt':
                l = CV.objects.get(user=u)
            else:
                l = Com.objects.get(user=u)
        except:
            pass
        return render(request, 'info.html', {'u': u, 'l': l})
    else:
        return redirect('/register')


def ch(request, id):
    r = Relation.objects.get(id=id)
    job = Zp.objects.filter(com=r.com)
    u = User.objects.get(username=request.user)
    if u.last_name == 'qy':
        return render(request, 'view.html', {'r': r, 'job': job})
    else:
        return render(request, 'cZp.html', {'r': r})


def send(request, id):
    r = Relation.objects.get(id=id)
    r.zp = request.get('zp')


def make(request, zp):
    u = User.objects.get(username=request.user)
    if u.last_name == 'qy':
        # if u.last_name == 'pt':
        return HttpResponse('对不起,您不是求职者')
    else:
        job = Zp.objects.get(id=zp)
        cv = CV.objects.get(user=u)
        try:
            if Relation.objects.get(com=job.com, zp=job, cv=cv):
                return HttpResponse('重复投递')
            else:
                r = Relation()
                r.com = job.com
                r.cv = cv
                r.zp = job
                r.save()
                return HttpResponse('投递成功')
        except:
            r = Relation()
            r.com = job.com
            r.cv = cv
            r.zp = job
            r.save()
            return HttpResponse('投递成功')


def invate(request, cv):
    u = User.objects.get(username=request.user)
    cv = CV.objects.get(id=cv)
    com = Com.objects.get(user=u)
    try:
        if Relation.objects.get(com=com, cv=cv):
            return HttpResponse('重复邀请')
        else:
            r = Relation()
            r.com = com
            r.cv = cv
            r.save()
            return HttpResponse('请处理面试信息')
    except:
        r = Relation()
        r.com = com
        r.cv = cv
        r.save()
        return HttpResponse('请处理面试信息')


def deal_invate(request, id):
    r = Relation.objects.get(id=id)
    job = Zp.objects.get(com=r.com, jobName=request.POST.get('job_name'))
    r.zp = job
    r.location = request.POST.get('location')
    r.tim = request.POST.get('tim')
    r.need = request.POST.get('need')
    r.is_have = True if request.POST.get('状态') == '已面试' else False
    r.result = True if request.POST.get('result') == '通过' else False
    r.save()
    return redirect('/deal')


def check(request):
    if request.user.is_authenticated:
        u = User.objects.get(username=request.user)
        # print(u.last_name)
        if u.last_name == 'qy':
            com = Com.objects.get(user=u)
            r = Relation.objects.filter(com=com)
            return render(request, 'deal.html', {'r': r})
        else:
            cv = CV.objects.get(user=u)
            r = Relation.objects.filter(cv=cv, is_have=False)
            return render(request, 'deal.html', {'r': r})
    else:
        regist = register(request)
        return regist


def delet(request, id):
    zp = Zp.objects.get(id=id)
    r = Relation.objects.filter(zp=zp)
    zp.delete()
    for i in r:
        i.delete()
    return redirect('/me')


def show_job(request):
    com = Com.objects.get(user=request.user)
    zp = Zp.objects.filter(com=com)
    return render(request, 'job.html', {'zp': zp})


def change(request, id):
    if request.method == 'GET':
        zp = Zp.objects.get(id=id)
        return render(request, 'ch_job.html', {'zp': zp})
    elif request.method == 'POST':

        Zp.objects.filter(id=id).update(jobName=request.POST.get('jobName'), jobTitle=request.POST.get('jobTitle'),
                  jobType=request.POST.get('jobType'), jobprofile=request.POST.get('jobprofile'),
                  number=request.POST.get('number'), academic=request.POST.get('academic'),
                  pre=request.POST.get('pre'), welfare=request.POST.get('welfare'),
                  need_number=request.POST.get('need_number'))
        return HttpResponse('修改成功')


def page_not_found(request):
    return render(request, '404.html')
