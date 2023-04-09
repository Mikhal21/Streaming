from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('movie/<int:movie_id>', views.movie, name='movie'),
    path('user/<int:user_id>', views.user, name='user')
]
