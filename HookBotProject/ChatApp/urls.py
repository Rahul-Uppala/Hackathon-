from django.urls import path
from . import views

urlpatterns = [
    path('chat/', views.chat_view, name='chat'),
    path('api/chatgpt/', views.chatgpt_api, name='chatgpt_api'),
    # Add more URL patterns if needed
]

