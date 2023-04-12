from . import views
from django.urls import  path


urlpatterns=[
    path('',views.homepage,name="homepage"),
    path('uploaded',views.uploaded,name='uploaded'),
    path('upload/', views.uploaded, name='upload_file'),
    path('serve/<path:file_path>/', views.serve_file, name='serve_file'),

     ]