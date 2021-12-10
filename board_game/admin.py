from django.contrib import admin

# Register your models here.
from .models import Game, Rent

admin.site.register(Game)
admin.site.register(Rent)