
from django.urls import path
from .import views

app_name = 'Post'

urlpatterns = [
    
    path('',views.posts, name="list"),
    path('create/',views.post_create, name='create'),
    path('<slug:slug>/',views.post_detail, name="detail"),
]
