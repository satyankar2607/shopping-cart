from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index1, name='index1'),
    path('index', views.index, name='index'),
    path('login', views.login, name='login'),
    path('logch', views.logch, name='logch'),
    path('signup', views.signup, name='sigup'),
    path('adm',views.adm, name='adm'),
    path('user',views.user, name='user'),
    path('add',views.add, name='add'),
    path('upd',views.upd, name='upd'),
    path('dele',views.dele, name='dele'),
    path('showlist',views.showlist,name='showlist'),
    path('mycart',views.mycart,name='mycart'),
    path('showcart/<str:product>/<str:price>/',views.showcart,name='showcart'),
    path('delcart/<str:product>/',views.delcart,name='delcart'),

]
