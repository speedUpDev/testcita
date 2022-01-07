from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='Citadel'),
    path('news/', news, name='news'),
    path('media/', video, name='media'),
    path('photos/', photos, name='photos'),
    path('player/', player, name='player'),
    path('streams/', streams, name='streams'),
    path('streams/', video, name='video'),
    path('article/', article, name='article'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('registration/', RegisterUser.as_view(), name='registration'),
    # path('news/<int:articleid>/', news)
]
