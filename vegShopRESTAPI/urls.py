from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from . import views
from .views import signin, user_info



router = routers.DefaultRouter()
router.register(r'vegitable', views.vegitableView, basename='vegitableView')
router.register(r'order', views.orderView, basename='orderView')
router.register(r'users', views.usersView, basename='usersView')

urlpatterns = [
    path('signin', signin),
    path('user_info', user_info),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]