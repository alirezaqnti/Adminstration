from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.test import TestCase

from .models import *


class PersonelTest(TestCase):
    def setUp(self) :
        Personel.objects.create(first_name='Alireza',last_name='Qanati',Phone='09177831766',NationalID='0371530601')
        Group.objects.create(name ='DEV')
        content_type = ContentType.objects.get_for_model(Personel) 
        permission = Permission.objects.create(
        codename='can_fly',
        name='can read books',
        content_type=content_type,
        )
        
        
        

    def test_personel_can_be_restricted(self):
        p = Personel.objects.get(first_name='Alireza',last_name='Qanati')
        gp  = Group.objects.get(name='DEV')
        per = Permission.objects.get(name='can read books')
        gp.permissions.add(per)
        p.groups.add(gp)
        self.assertEqual(p.get_full_name(),'Alireza Qanati','FAILED PERSONEL')
        self.assertEqual(gp.name,'DEV','FAILED GROUP')


class TeamTest(TestCase):
    def setUp(self) :
        Team.objects.create(Name='DEVTEAM',Description='DEV Team Description')
        Group.objects.create(name ='DEV')
        content_type = ContentType.objects.get_for_model(Team) 
        permission = Permission.objects.create(
        codename='can_book',
        name='can read books',
        content_type=content_type,
        )        

    def test_team_can_be_restricted(self):
        p = Team.objects.get(Name='DEVTEAM')
        gp  = Group.objects.get(name='DEV')
        per = Permission.objects.get(name='can read books')
        gp.permissions.add(per)
        p.Access = gp
        p.save()
        self.assertEqual(p.Name,'DEVTEAM','FAILED TEAM')
        self.assertEqual(gp.name,'DEV','FAILED GROUP')