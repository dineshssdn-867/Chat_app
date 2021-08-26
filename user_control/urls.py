from django.urls import path, include
from .views import LoginView, RegisterView, RefreshView
from rest_framework.routers import DefaultRouter
from .views import *


router = DefaultRouter(trailing_slash = False)

router.register(r"profile", UserProfileView)

urlpatterns = [
    path('', include(router.urls)),
    path('login', LoginView.as_view()),
    path('register', RegisterView.as_view()),
    path('refresh', RefreshView.as_view()),
    path('me', MeView.as_view()),
    path('logout', LogoutView.as_view()),
] 
