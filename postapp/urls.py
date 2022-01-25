from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'postapp'

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

    # img upload
    path('upload1/', views.upload1, name='upload1'),
    path('upload2/', views.upload2, name='upload2'),
    path('upload3/', views.upload3, name='upload3'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
