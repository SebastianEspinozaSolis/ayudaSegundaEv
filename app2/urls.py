from django.urls import path
from . import views
app_name = 'app2'
urlpatterns = [
 path('vista1/', views.vista1_app2, name='vista1_app2'),
 path('vista2/', views.vista2_app2, name='vista2_app2'),
]