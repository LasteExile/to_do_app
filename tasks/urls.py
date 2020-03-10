from django.urls import path

from . import views


urlpatterns = [
    path('', views.Home.as_view(), name='home_page'),
    path('create', views.CreateTask.as_view(), name='create_page'),
    path('detail/<int:pk>', views.Detail.as_view(), name='detail_page'),
    path('about', views.About.as_view(), name='about_page'),
]
