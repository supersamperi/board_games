from django import forms

from .models import Game, Rent

class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['name', 'maker', 'year_published', 'description']
        labels = {'name': 'Nimi', 'maker': 'Julkaisija', 'year_published': 'Valmistusvuosi', 'description': 'Kuvaus'}

class RentForm(forms.ModelForm):
    class Meta:
        model = Rent
        fields = ['game', 'stars', 'renter', 'review']
        labels = {'game': 'Peli', 'stars': 'Tähdet', 'renter': 'Lainaaja', 'review': 'Arvostelu'}
        
