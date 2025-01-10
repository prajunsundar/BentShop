from django.urls import path
from .views import Register,Login,Logout,Account,UserProfile
app_name='userapp'

urlpatterns=[
    path('register/',Register,name='register'),
    path('profile/',UserProfile,name='profile'),
    path('login/',Login,name='login'),
    path('logout/',Logout,name='logout'),
    path('account/',Account,name='account'),




]