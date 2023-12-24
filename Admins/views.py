from django.core.cache import cache
from django.http.response import JsonResponse
from django.shortcuts import render
from django.views.generic import FormView
from rest_framework.response import Response
from rest_framework.views import APIView

from .forms import TeamForm
from .models import Team


def TeamData():
    if not 'TEAMS' in cache:
        res = {}
        TEAMS = []
        T = Team.objects.all().prefetch_related('ques_team','thread_team','task_team','ticket_team').order_by('-Created')
        [TEAMS.append(x.toJson()) for x in T]

        res['Teams'] = TEAMS
        cache.set('TEAMS',res,60*15)
    else:
        res = cache.get('TEAMS')
    return res

class GetTeamData(APIView):
    def get(self, request, *args, **kwargs):
        res = TeamData()
        return Response(res)

class NewTeamReg(FormView):
    form_class = TeamForm

    def form_valid(self, form):
        form.save()
        print(form)
        cache.delete('TEAMS')
        return JsonResponse({"stat":200})