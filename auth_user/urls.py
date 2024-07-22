from django.contrib import admin
from django.urls import path
from task import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home, name='home'),

    path('signup/', views.signup, name='signup'),

    path('signin/', views.signin, name='signin'),

    path('signout/', views.signout, name='signout'),
    
    path('tasks/', views.tasks, name='tasks')

    
]
