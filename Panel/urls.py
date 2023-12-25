from django.urls import path

from . import views

urlpatterns = [
    path('',views.redToHome),
    path('dashboard/',views.DashboardView.as_view(),name='Dashboard'),
    path('teams/',views.TeamsView.as_view(),name='TeamsView'),
    path('personel/',views.PersonelView.as_view(),name='PersonelView'),
    path('logout/',views.LogoutView.as_view(),name='LogoutView'),
    path('login/',views.LoginView.as_view(),name='LoginView'),
    path('login/authentiction/',views.LoginAPIView.as_view(),name='LoginAPIView'),
]
