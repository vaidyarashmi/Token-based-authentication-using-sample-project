from django.urls import path,include
from testapp import views
urlpatterns = [
    path('api/', views.login),
    path('sample/', views.sample_api),
]
