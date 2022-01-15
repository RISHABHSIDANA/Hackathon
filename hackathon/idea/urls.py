from django.urls import path
from idea import views

urlpatterns = [
   path('', views.ProfileUserList.as_view(), name='user-list'),
]