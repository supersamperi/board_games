from django.shortcuts import render, redirect

from .models import Game, Rent
from .forms import GameForm, RentForm

# Create your views here.

def index(request):
    """The home page for Board games"""
    return render(request, 'board_game/index.html')

def games(request):
    """show all games"""
    games = Game.objects.order_by('date_added')
    context = {'games': games}
    return render(request, 'board_game/games.html', context)

def game(request, game_id):
    """Show a single game and all its rent data"""
    game = Game.objects.get(id=game_id)
    rents = game.rent_set.order_by('-date_added')
    context = {'game': game, 'rents': rents}
    return render(request, 'board_game/game.html', context)

def new_game(request):
    """add a new game"""
    if request.method !='POST':
        # No data submitted; create a blank form.
        form = GameForm()
    else:
        # Post data submitted; process data
        form = GameForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('board_game:games')
    # Display a blank or invalid form
    context = {'form': form}
    return render(request, 'board_game/new_game.html', context)

def new_rent(request, game_id):
    """Add a new rent for a game"""
    game = Game.objects.get(id=game_id)

    if request.method !='POST':
        # no data submitted; create a blank form
        form = RentForm()
    else:
        # POST data submitted; process data
        form = RentForm(data=request.POST)
        if form.is_valid():
            new_rent = form.save(commit=False)
            new_rent.game = game
            new_rent.save()
            return redirect('board_game:game', game_id=game_id)
    
    # Display a blank or invalid form
    context = {'game': game, 'form': form}
    return render(request, 'board_game/new_rent.html', context)

