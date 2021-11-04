from django.contrib import admin
from django.urls import path, include
from  todo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todo.urls')),
    path('home/',views.home, name="home"),
    path('new/',views.new, name="new"),
    path('base/',views.base, name="base"),
]
