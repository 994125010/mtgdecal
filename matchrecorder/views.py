from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.template import loader
from registration.forms import RegistrationForm
from .models import Match, Player


def index(request):
    return HttpResponse("Hello World. You are at the matchrecorder index.")

def player_history(request, player_id):
    match_list = Match.objects()
    template = loader.get_template('matchrecorder/index.html')
    context = {
        'match_list': match_list,
    }
    return HttpResponse(template.render(context, request))

def weekly_recap(request, week_id):
    return HttpResponse("Matches/games record for week {0}".format(week_id))

def record_game(request, player_id):
    return HttpResponse("Record matches/games for player {0}".format(player_id))

