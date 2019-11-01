from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('',views.list, name = 'list'),
    path('new/', views.new, name = 'new'),
    path('create/', views.create, name = 'create'),
    path('<int:pk>/', views.detail, name = 'detail'), #primery-key
    path('<int:pk>/delete/', views.delete, name = 'delete'),
    path('<int:pk>/edit/', views.edit, name = 'edit'),
    path('<int:pk>/update/', views.update, name = 'update'),
    path('detail/',views.detail, name = 'detail'),
    
    
]