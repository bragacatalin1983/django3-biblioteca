
from django.urls import path,include
from . import views

app_name='blog'

urlpatterns = [
    path('',views.all_blogs, name='all_blogs'),
    path('<int:nr_id>/',views.blog_id,name='blog_id')
    ]
