from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('scrap',views.scrap, name='scrap'),
    path('data',views.data, name='data'),
    path('topicmodelling',views.topicModeling, name='topicmodelling'),
]