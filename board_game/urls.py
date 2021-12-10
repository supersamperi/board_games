"""Defines URL patterns for board_game"""
from django.urls import path

from . import views

app_name = 'board_game'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # page that shows all the games
    path('games/', views.games, name='games'),
    # detail page for a single game
    path('games/<int:game_id>/', views.game, name='game'),
    # page for adding a new game
    path('new_game/', views.new_game, name='new_game'),
    # page for adding a new rent
    path('new_rent/<int:game_id>', views.new_rent, name='new_rent'),
    # page for editing rent
    path('edit_rent/<int:rent_id>/', views.edit_rent, name='edit_rent')
]