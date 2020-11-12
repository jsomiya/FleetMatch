from django.contrib import admin
from django.urls import path
from knox import views as knox_views

from .views import LoginAPI, SignupAPI, Register
from managers.views import all_service_partners, filter_partners

urlpatterns = [
    path('api/signup/', SignupAPI.as_view(), name = "signup"),
    path('api/login/', LoginAPI.as_view(), name = "login"),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('api/register/', Register.register, name = "register"),
    path('api/dashboard/', Register.dashboard , name = "dashboard"),
    path('api/delete_profile/', Register. delete_profile, name = "delete_profile"),
    path('api/update_profile/', Register.update_profile , name = "update_profile"),
    path('api/all_service_partners/', all_service_partners, name = "all_service_partners"),
    path('api/filter_partners/', filter_partners, name = "filter_partners"),

]