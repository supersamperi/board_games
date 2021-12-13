from django import forms

from .models import Game, Rent

class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['name', 'maker', 'year_published', 'description', 'owner']
        labels = {'name': 'Nimi', 'maker': 'Julkaisija', 'year_published': 'Valmistusvuosi', 'description': 'Kuvaus', 'owner': 'Omistaja', 'rented': 'lainassa'}

class RentForm(forms.ModelForm):
    class Meta:
        model = Rent
        fields = ['game', 'stars', 'renter', 'review', 'rented']
        labels = {'game': 'Peli', 'stars': 'Tähdet', 'renter': 'Lainaaja', 'review': 'Arvostelu', 'rented': 'Lainassa:'}
        
