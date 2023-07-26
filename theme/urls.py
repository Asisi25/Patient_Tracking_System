from django.urls import path
from . import views
app_name = 'theme'

urlpatterns = [
    path('', views.index, name='index'),
    path('blog-details/', views.blog_details, name='blog-details'),
    path('index-2/', views.index2, name='index-2'),
]