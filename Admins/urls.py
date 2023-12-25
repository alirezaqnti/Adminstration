from django.urls import path

from . import views

urlpatterns = [
    path('get-personel-data/',views.GetPersonelData.as_view(),name='GetPersonelData'),
    path('get-team-data/',views.GetTeamData.as_view(),name='GetTeamData'),
    path('new-team-register/',views.NewTeamReg.as_view(),name='NewTeamReg'),
    path('new-personel-register/',views.NewPersonelReg.as_view(),name='NewPersonelReg')
]
