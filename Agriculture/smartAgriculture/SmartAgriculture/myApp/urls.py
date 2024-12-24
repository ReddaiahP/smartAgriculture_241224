
from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.home, name = 'home'),
    path('predect/', views.predect, name = 'predect'),
    path('result/', views.result, name = 'result'),
]
