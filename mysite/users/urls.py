import router as router
from . import views as admin_views, views, admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('login/', views.sign_in, name="login"),
    path('logout/', views.sign_out, name='logout'),
    path('register/', views.sign_up, name="register"),
    path('find_account/', views.change_password, name="find_account"),
    path('pw_reset/', auth_views.PasswordResetView.as_view(), name="pw_reset"),
    path('profile/', views.Myprofile, name='profile'),

    path('api/', include(router.urls)),  # Include the API URLs from the router
]

