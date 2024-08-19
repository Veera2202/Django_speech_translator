from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('recognize/', views.recognize_speech, name='recognize_speech'),
    path('translate/', views.translate_speech, name='translate_speech'),
    path('translate_text/', views.translate_text, name='translate_text'),  # Add this line
]