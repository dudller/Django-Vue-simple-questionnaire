
from . import views
from django.urls import path

app_name = 'ankieta'
urlpatterns = [
    path('', views.index, name='index'),
    path('vote/', views.vote, name='vote'),
    path('end/',views.end,name='end'),
]
