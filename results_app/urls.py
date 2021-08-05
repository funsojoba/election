from django.urls import path
from .views import index, get_lga, get_pu

urlpatterns = [
    path('', index, name="index"),
    path('lga/<str:pk>', get_lga, name="get_lga"),
    path('pu-results/<str:pk>', get_pu, name="polling_unit")
]
