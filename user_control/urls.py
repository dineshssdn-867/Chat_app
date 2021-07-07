from django.urls import path, include
from .views import LoginView, RegisterView, RefreshView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('login', LoginView.as_view()),
    path('register', RegisterView.as_view()),
    path('refresh', RefreshView.as_view()),
] + static(settings.MEDIA_URL)