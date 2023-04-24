

from django.urls import path,include
from . import views

urlpatterns = [
    path('treg', views.tregister,name="treg"),
    path('tlog',views.tlog,name="tlog"),
    path('tmssg',views.tmssg,name="tmssg"),
    path('tpage',views.tpage,name="tpage"),
    path('tprofile',views.tprofile,name="tprofile"),
    path('question',views.question,name="question"),
    path('teditprofile/<int:id>',views.teditprofile,name="teditprofile"),
    path('vques',views.view_ques,name="vques"),

    path('evaluate/<int:id>',views.Evaluation,name="evaluate"),

]


