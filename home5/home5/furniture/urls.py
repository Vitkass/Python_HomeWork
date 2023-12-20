from django.urls import path

from . import views

app_name = 'furniture'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:furniture_id>/', views.detail, name='detail'),

]
