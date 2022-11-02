from django.urls import path, include

from .views import USERCreate, Login, SERVER_list, SERVER_C,SERVER_detail

urlpatterns = [
    path('CUS', USERCreate),
    path('LG', Login),
    path('SL/<int:pk>', SERVER_list),
    path('SV/', SERVER_C),
    path('SV/<int:pk>', SERVER_detail),
]
