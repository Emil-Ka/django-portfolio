from django.urls import path, include
from . import views

app_name = 'blog'

urlpatterns = [
  path('', views.blog),
  path('all_blogs/', views.all_blogs),
  path('<int:blog_id>/', views.detail, name='detail'),
]