from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import Group
from django.core.cache import cache
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import redirect, render
from django.views.generic import FormView, RedirectView, TemplateView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from Admins.forms import PersonelForm, TeamForm
from Admins.models import Personel, Team
from Admins.views import PersonelData, TeamData
from core import settings


@login_required()
def redToHome(request):
    return redirect('Dashboard')

class BaseView (LoginRequiredMixin,TemplateView):
    login_url = settings.LOGIN_URL

class DashboardView(BaseView):
    template_name = "Dashboard.html"
    
class LoginView(TemplateView):
    template_name = "Login.html"
    def get(self, request, *args, **kwargs):
        print(request.user.is_authenticated)
        if request.user.is_authenticated:
            return redToHome(request)
        return super().get(request, *args, **kwargs)

class LoginAPIView(APIView):
    def post(self, request, *args, **kwargs):
        un = request.data['username']
        ps = request.data['password']
        Name = ''
        stat = 404
        try:
            user = Personel.objects.get(Q(Phone=un) | Q(username=un))
            if user.check_password(ps):
                login(request, user)
                Name = user.get_full_name()
                stat = 200
        except:
            pass
        return Response({'Name':Name,'stat':stat})

class LogoutView(LoginRequiredMixin,RedirectView):
    url = settings.LOGOUT_REDIRECT_URL
    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogoutView,self).get(request, *args, **kwargs)
    
class TeamsView(BaseView):
    template_name = 'Teams.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        res = TeamData()
        form = TeamForm()    
        pp = self.request.GET.get('pp','15')
        page = self.request.GET.get('page','1')
        paginator = Paginator(res["Teams"],int(pp))
        OBJ = paginator.get_page(int(page))
        context["TEAMS"] = OBJ
        context["Form"] = form
        return context

class PersonelView(BaseView):
    template_name = 'Personel.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        res = PersonelData()
        form = PersonelForm()    
        pp = self.request.GET.get('pp','15')
        page = self.request.GET.get('page','1')
        paginator = Paginator(res["Personel"],int(pp))
        OBJ = paginator.get_page(int(page))
        context["PERSONEL"] = OBJ
        context["Form"] = form
        return context

    
    
    
