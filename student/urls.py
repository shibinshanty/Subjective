

from django.urls import path,include
from . import views

urlpatterns = [
    path('sreg', views.sreg,name="sreg"),
    path('slog',views.slog,name="slog"),
    path('spage',views.spage,name="spage"),
    path('sprofile',views.sprofile,name="sprofile"),
    path('seditprofile/<int:id>',views.seditprofile,name="seditprofile"),
    path('viewquestion',views.viewquestion,name="viewquestion"),
    path('answer<int:id>',views.answer,name="answer"),
    path('smssg',views.smssg,name="smssg"),
    path('mdet',views.markdet,name="mdet"),



    
    
    ]


