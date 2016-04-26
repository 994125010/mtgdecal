from django.db import models
from django.contrib.auth.models import User
import uuid

class Player(models.Model):
    DCI = models.PositiveIntegerField(unique=True, default=uuid.uuid4)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tournaments = models.CharField(max_length=5000, default='[]') # str of tournament_ids

DEFAULT_HO = 0
class Tournament(models.Model):
    host = models.ForeignKey(Player, default=DEFAULT_HO)
    name = models.CharField(max_length=200)
    desc = models.CharField(max_length=1000)

DEFAULT_P1 = 0
DEFAULT_P2 = 1
DEFAULT_TO = 0
class Match(models.Model):
    player1 = models.ForeignKey(Player, default=DEFAULT_P1, related_name='winner') # winner by default
    player2 = models.ForeignKey(Player, default=DEFAULT_P2, related_name='loser') # loser by default
    wins = models.PositiveIntegerField(default=0) # player1 wins
    loss = models.PositiveIntegerField(default=0) # player1 loss
    ties = models.PositiveIntegerField(default=0)
    date_submitted = models.DateTimeField('date submitted')
    tournament = models.ForeignKey(Tournament, default=DEFAULT_TO)


