from django.urls import path
from . import views


urlpatterns = [
    path('', views.denunc_list, name='denunc_list'),
    path('denunc/<int:pk>/', views.denunc_detail, name='denunc_detail'),
    path('denunc/new/', views.denunc_new, name='denunc_new'),
    path('denunc/<int:pk>/edit/', views.denunc_edit, name='denunc_edit'),
    path('register/', views.register_view, name='register'),
    path('profil/', views.profil, name='profil'),
    
]
