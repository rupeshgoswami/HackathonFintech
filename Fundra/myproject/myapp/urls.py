from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('crypto-sentiment/', views.crypto_sentiment, name='crypto_sentiment'),
]
