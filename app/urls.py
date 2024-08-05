from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("login", views.inicio_sesion,name="login"),
    path("register", views.registro,name="register"),
    path('vendedor', views.vendedor_home, name='vendedor_home'),
    path('logout/', views.cerrar_sesion, name='logout'),
]
