from django.urls import path
from . import views
urlpatterns = [
    path('login/', views.login, name='login'),
    # Add other URL patterns for this app if needed
]