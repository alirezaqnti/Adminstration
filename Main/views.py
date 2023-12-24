# from django.shortcuts import render
import random
import string
from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Permission, User
from django.contrib.contenttypes.models import ContentType


def RandInt(prefix):
    d = datetime.now().strftime("%Y%S")
    return f"{prefix}-{d}{str(random.randint(1000,9999))}"


def RandString():
    letters = string.ascii_uppercase
    result_str = "".join(random.choice(letters) for i in range(6))
    return result_str

def CreateNewPermission(Model,Code,Name):
    content_type = ContentType.objects.get_for_model(Model) 
    permission = Permission.objects.create(
        codename=Code,
        name=Name,
        content_type=content_type,
    )
    return permission
def get_user_group_names(self):
    gp = self.groups.all()
    arr = []
    for item in gp:
        arr.append(item.name)
    print(arr)
    return arr

User.add_to_class('get_user_group_names',get_user_group_names)