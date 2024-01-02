from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import Group
from django.core.cache import cache
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import redirect, render
from django.views.generic import FormView, RedirectView, TemplateView
from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from Admins.forms import PersonelForm, TeamForm
from Admins.models import Personel, Team
from Admins.views import PersonelData, TeamData
from core import settings
from Main.serializers import PhoneCodeRegSerializer
from Main.views import Code

from .permissions import LoginRequiredPermission


@login_required()
def redToHome(request):
    return redirect('Dashboard')

class BaseView (LoginRequiredPermission,TemplateView):
    login_url = settings.LOGIN_URL

class DashboardView(BaseView):
    template_name = "Dashboard.html"
    def get(self, request, *args, **kwargs):

        return super().get(request, *args, **kwargs)
    
class LoginView(TemplateView):
    template_name = "Login.html"
    def get(self, request, *args, **kwargs):
        print(request.user.is_authenticated)
        if request.user.is_authenticated:
            return redToHome(request)
        return super().get(request, *args, **kwargs)

class LoginPassAPIView(APIView):
    def post(self, request, *args, **kwargs):
        un = request.data['username']
        ps = request.data['password']
        Name = ''
        stat = 404
        user = Personel.objects.get(Q(Phone=un) | Q(username=un))
        try:
            print(user)
            if user.check_password(ps):
                login(request, user)
                Name = user.get_full_name()
                stat = 200
        except:
            pass
        return Response({'Name':Name,'stat':stat})

class LoginPhoneAPIView(APIView):
    def post(self, request, *args, **kwargs):
        Phone = request.data['Phone']
        try:
            user = Personel.objects.get(Phone=Phone)
            Code(Phone)
            stat = 200
            report = f'کد اعتبارسنجی به شماره {Phone} ارسال شد.'
        except:
            stat = 404
            report = f'کاربری شماره وارد شده یافت نشد!'
        return Response({'stat':stat,'report':report})

class LoginCodeCheckAPI(APIView):
    def post(self, request, *args, **kwargs):
        serializer = PhoneCodeRegSerializer(data=request.data)
        stat = 500
        report = "اطلاعات ارسال شده صحیح نیست"
        if serializer.is_valid():
            stat = 200
            try:
                user = Personel.objects.get(Phone=request.data["Phone"])
                login(request,user)
                request.data["Phone"]
                request.data["Code"]
                stat = 200
                context = {"Name": user.get_full_name(), "stat": stat}
                return Response(context, status=status.HTTP_200_OK)
            except:
                pass
        print(serializer.errors)
        context = {"report": report, "stat": stat}
        return Response(context)

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

class SetLoginInfo(LoginRequiredMixin,TemplateView):
    template_name='NewPersonel.html'
    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']
        User = request.user
        User.password = make_password(password)
        User.username = username
        User.save()
        return redirect('Dashboard')
    
class UsernameCheck(APIView):
    def post(self, request, *args, **kwargs):
        stat = 500
        username = request.data['username']
        try:
            Personel.objects.get(username=username)
        except:
            stat = 200
        return Response({'stat':stat})


class PersonelInfo(BaseView):
    template_name = "PersonelInfo.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        SPE = self.kwargs['SPE']
        PE = Personel.objects.filter(SPE=SPE).prefetch_related('offreq_personel','address_pers','respond_pers','assign_pers','edu_personel','exp_personel').first()
        
        context["Person"] = PE
        context["EDU"] = PE.edu_personel.all()
        context["EXP"] = PE.exp_personel.all()
        # context["Address"] = PE.address_pers.last()
        return context
    
