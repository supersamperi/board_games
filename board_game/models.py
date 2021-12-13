from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

# Creating a model for the board games
class Game(models.Model):
    """Board games that are on the list"""
    name = models.CharField(max_length=200)
    maker = models.CharField(max_length=20)
    year_published = models.IntegerField()
    description = models.CharField(max_length=200)
	
    """Adding date added and date modified fields that are automatic"""
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    # Creating a model for renting the board games
class Rent(models.Model):
    """user renting the game"""
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    """setting validators so the user can only giver stars from 1 to 5"""
    stars = models.PositiveIntegerField(null=True,
        validators=[MinValueValidator(1),
        MaxValueValidator(5)],)
    renter = models.CharField(max_length=30)
    review = models.CharField(max_length=255)
    rented = models.BooleanField()

    """Adding date added and date modified fields that are automatic"""
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name_plural = 'Rent'
    
    def __str__(self):
        """return review representation of the model"""
        return self.renter