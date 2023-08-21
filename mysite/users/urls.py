from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.sign_in,name="login"),
    path('logout/',views.sign_out, name='logout'),
    path('register/',views.sign_up, name="register"),
    path('find_account/',views.change_password, name="find_account"),
]
