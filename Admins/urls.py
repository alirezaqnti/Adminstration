from django.urls import path

from . import views

urlpatterns = [
    path('get-team-data/',views.GetTeamData.as_view(),name='GetTeamData'),
    path('new-team-register/',views.NewTeamReg.as_view(),name='NewTeamReg')
]
