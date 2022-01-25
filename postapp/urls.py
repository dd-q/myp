from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.postlist, name='postlist'),
    path('<int:id>/', views.postlist_id, name='postlist_id'),
    path('show/<int:id>/', views.show, name = 'show'),
    # Create
    path('new/', views.new, name = 'new'),
    path('postcreate/', views.postcreate, name = 'postcreate'),

    # Update
    path('edit/', views.edit, name ='eidt'),
    path('postupdate/<int:id>', views.postupdate, name ='postupdate'),

]
