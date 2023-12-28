from django.urls import path

from . import views

urlpatterns = [
    path('',views.redToHome),
    path('dashboard/',views.DashboardView.as_view(),name='Dashboard'),
    path('dashboard/set-login-info/',views.SetLoginInfo.as_view(),name='SetLoginInfo'),
    path('dashboard/set-login-info/username-check/',views.UsernameCheck.as_view(),name='UsernameCheck'),
    path('teams/',views.TeamsView.as_view(),name='TeamsView'),
    path('personel/',views.PersonelView.as_view(),name='PersonelView'),
    path('logout/',views.LogoutView.as_view(),name='LogoutView'),
    path('login/',views.LoginView.as_view(),name='LoginView'),
    path('login/authentiction/password/',views.LoginPassAPIView.as_view(),name='LoginAPIView'),
    path('login/authentiction/phone/code/',views.LoginPhoneAPIView.as_view(),name='LoginPhoneAPIView'),
    path('login/authentiction/phone/code/check/',views.LoginCodeCheckAPI.as_view(),name='LoginCodeCheckAPI'),
]
