from django.urls import path
from .views import index, get_lga

urlpatterns = [
    path('', index, name="index"),
    path('lga/<str:pk>', get_lga, name="get_lga")

]
