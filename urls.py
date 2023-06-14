from django.urls import path
from django.urls import path
from Svetkavichkata_app import views

urlpatterns = [
    path('register/', views.Register, name='register'),
    path('home/', views.home_page, name='home'),
    path('workers/', views.workers_page, name='workers'),
    path('arduinocar/', views.arduino_page, name='arduinocar'),
     path('login/', views.Login, name="login-page"),
    path('logout/', views.logoutuser, name='logout'),
]