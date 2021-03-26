from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    # localhost:8000/unicorn
    path('unicorn', views.unicorn),
    path('processed', views.processed),
    path('second', views.second),
    path('<url>', views.catch_all),
]