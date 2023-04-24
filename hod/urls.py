

from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.hod,name="hod"),
    path('hreg',views.hreg,name="hreg"),
    path('hlog',views.hlog,name="hlog"),
    path('hpage',views.hpage,name="hpage"),
    path('hprofile',views.hprofile,name="hprofile"),
    path('heditprofile/<int:id>',views.heditprofile,name="heditprofile"),
    path('hteacher',views.hteacher,name="hteacher"),
    path('tapprove<str:pk>',views.tapprove,name="tapprove"),
    path('tdlt<int:pid>',views.tdlt,name='tdlt'),
    path('hstudent',views.hstudent,name="hstudent"),
    path('sapprove<str:pk>',views.sapprove,name="sapprove"),
    path('sdlt<int:pid>',views.sdlt,name='sdlt'),
    path('sdet',views.studentdet,name="sdet"),


]


