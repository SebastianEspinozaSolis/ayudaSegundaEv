from django.urls import path
from . import views
app_name = 'app1'
urlpatterns = [
 path('vista1/', views.vista1_app1, name='vista1_app1'),
 path('vista2/', views.vista2_app1, name='vista2_app1'),
]