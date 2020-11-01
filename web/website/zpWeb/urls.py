"""zpWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from ZpModel.views import *
# from ZpModel import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', ZpListView.as_view()),
                  re_path(r'^list_.*', ZpListView.as_view()),
                  path('login', logIN),
                  path('logout', logOUT),
                  path('reg', reg),
                  path('register', register),
                  path('forgot', forgotPasswd),
                  path('me', me),
                  path('info', info),
                  re_path(r'^save_info/$', save_info),
                  re_path(r'^create_job/$', create_job),
                  # path('submit_me',view.submit_me),
                  path('job', show_job),
                  # path('view',bigDataView.v),
                  # path('tj',bigDataView.match_CV.as_view()),
                  path('jlpp', jl),
                  re_path('^invate/(?P<cv>\d+)/$', invate),
                  re_path('^make/(?P<zp>\d+)/$', make),
                  re_path('^ch/(?P<id>\d+)/$', ch),
                  re_path('^deal_invate/(?P<id>\d+)/$', deal_invate),
                  re_path('^delete/(?P<id>\d+)/$', delet),
                  path('deal', check),
                  re_path('^change/(?P<id>\d+)/$', change),

                  # path('collection',bigDataView.v),
                  #
                  # #path('j_main',bigDataView.j_main),

                  # 公司部分
                  # path('cIndex',cViews.cIndex),
                  # # path('cAppli',cViews.cAppli.as_view()),
                  # path('saveComInfo/', cViews.save_com_info),
                  # path('addZp', cViews.addZp),
                  # path('saveZp',cViews.saveZp),
                  # path('delZp',cViews.delZp),
                  # path('CVgo', view.CVgo),
                  # path('lookCV',cViews.lookCV),
                  # path('refuse',cViews.refuse),
                  # path('send',cViews.send)
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
