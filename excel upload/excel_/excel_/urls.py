from django.urls import path
from . import views
 
urlpatterns = [
    path("",views.base,name="base"),
    path("user_login/",views.user_login,name="user_login"),
 
  
 
    path('export_users_csv/', views.export_users_csv,name="export_users_csv"),  
    path('Import_csv/', views.Import_csv,name="Import_csv"),  
     
]