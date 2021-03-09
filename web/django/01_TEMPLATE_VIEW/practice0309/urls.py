from django.urls import path
from . import views

urlpatterns = [
    path('var_route/<int:value>/', views.var_route),
    # /practice0309/lotto/<회차>/
    path('lotto/<int:no>', views.lotto),
    path('ping/', views.ping, name="ping"),
    path('pong/', views.pong, name="pong"),
]
