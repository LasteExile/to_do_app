from django.urls import path

from . import views


urlpatterns = [
    path('', views.Home.as_view(), name='home_page'),
    path('create', views.CreateTask.as_view(), name='create_page'),
    path('detail/<int:pk>', views.Detail.as_view(), name='detail_page'),
    path('detail/<int:pk>/createsub', views.CreateSubTask.as_view(), name='createsub_page'),
    path('detail/<int:pk>/edit', views.EditTask.as_view(), name='edittask_page'),
    path('detail/<int:pk>/editsub/<int:pk1>', views.EditSubTask.as_view(), name='editsubtask_page'),
    path('about', views.About.as_view(), name='about_page'),
]
