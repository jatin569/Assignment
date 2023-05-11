from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload, name='upload'),
    path('admin_panel/', views.admin_panel, name='admin_panel'),
    path('download/<str:file_name>/', views.download, name='download'),
    path('open_file/<str:file_name>/', views.open_file, name='open_file'),
]
