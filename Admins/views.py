from django.contrib.auth.hashers import make_password
from django.core.cache import cache
from django.db.models import Q
from django.http.response import JsonResponse
from django.shortcuts import render
from django.views.generic.edit import FormView
from rest_framework.response import Response
from rest_framework.views import APIView

from Main.views import RandString

from .forms import PersonelForm, TeamForm
from .models import Personel, Team


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

def PersonelData():
    if not 'PERSONEL' in cache:
        res = {}
        PERSONEL = []
        T = Personel.objects.all().prefetch_related('offreq_personel').order_by('-Joined')
        [PERSONEL.append(x.toJson()) for x in T]

        res['Personel'] = PERSONEL
        cache.set('PERSONEL',res,60*15)
    else:
        res = cache.get('PERSONEL')
    return res

class GetPersonelData(APIView):
    def get(self, request, *args, **kwargs):
        res = PersonelData()
        return Response(res)

class GetTeamData(APIView):
    def get(self, request, *args, **kwargs):
        res = TeamData()
        return Response(res)

class NewTeamReg(FormView):
    form_class = TeamForm

    def form_valid(self, form):
        form.save()
        cache.delete('TEAMS')
        return JsonResponse({"stat":200})

class NewPersonelReg(APIView):
    def clean(self,form):
        print(form)
        cleaned_data = form.cleaned_data
        Phone = cleaned_data["Phone"]
        NationalID = cleaned_data["NationalID"]
        try:
            PE = Personel.objects.get(Q(Phone=Phone) | Q(NationalID=NationalID))
            print(PE)
            return False
        except:
            return super().clean()
    def form_valid(self, form):
        
        f = form.save()
        f.username = RandString()
        f.password = make_password(None)
        f.save()
        cache.delete('PERSONEL')
        return JsonResponse({"stat":200})
    
    def post(self, request, *args, **kwargs):
        report = ''
        stat = 500
        form = PersonelForm(request.POST)
        Phone = request.data['Phone']
        NationalID = request.data['NationalID']
        try:
            PE = Personel.objects.get(Q(Phone=Phone) | Q(NationalID=NationalID))
            stat = 500
            report = 'کاربر دیگری با این شماره تماس یا کد ملی موجود است'
            print(PE)
        except:
            if form.is_valid():
                self.form_valid(form)
                stat = 200
            else:
                stat = 500
        return Response({'stat':stat,'report':report})